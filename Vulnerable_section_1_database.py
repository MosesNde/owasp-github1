 
         return model
 
    def firstWhere(self, col: str, val: str, additional=""):
         with DataBaseConnection() as db:
             sql = self._buildQuery(
                 f"SELECT * FROM {self.model.table}",
                f"WHERE {col} = '{val}' {additional}",
             )
 
            db.cursor.execute(sql)
             data = db.cursor.fetchone()
 
         return self._loadWithLogic(data) if data else None
 
     def Where(self, col: str, val: str):
         with DataBaseConnection() as db:
             sql = self._buildQuery(
                f"SELECT * FROM {self.model.table}", f"WHERE {col} = '{val}'"
             )
 
            db.cursor.execute(sql)
             data = db.cursor.fetchall()
 
         return [self._loadWithLogic(r) for r in data] if data else None
 
     def WhereLike(self, col: str, val: str):
         with DataBaseConnection() as db:
             sql = self._buildQuery(
                f"SELECT * FROM {self.model.table}", f"WHERE {col} like '%{val}%'"
             )
 
            print(sql)

            db.cursor.execute(sql)
             data = db.cursor.fetchall()
 
         return [self._loadWithLogic(r) for r in data] if data else None
 
     def createIfNotExists(self, model):
         if self.model.unique and self.firstWhere(
            self.model.unique, getattr(model, self.model.unique)
         ):
             return None
         else:
             with DataBaseConnection() as db:
                vals = ",".join(
                    f"'{e}'" if e is not None else "NULL"
                    for e in [getattr(model, a) for a in self.model.fillable]
                )
                 cols = ",".join(self.model.fillable)
                 db.cursor.execute(
                    f"INSERT INTO {self.model.table} ({cols}) VALUES ({vals})"
                 )
                 setattr(model, "id", db.cursor.lastrowid)
         return model
 
     def update(self, model):
         if self.model.unique and self.firstWhere(
            self.model.unique,
            getattr(model, self.model.unique),
            additional=f"AND id != {model.id}",
         ):
             return None
         else:
             with DataBaseConnection() as db:
                vals = [
                    f"'{e}'" for e in [getattr(model, a) for a in self.model.fillable]
                ]
                 cols = self.model.fillable

                update = []
                for i, col in enumerate(cols):
                    update.append(f"{col} = {vals[i]}")

                db.cursor.execute(
                    f"UPDATE {self.model.table} SET {','.join(update)} WHERE id = {model.id}"
                )
         return True
 
     def hasMany(self, model, mtm, m_col, f_col):
         with DataBaseConnection() as db:
            sql = f"SELECT {self.model.table}.* FROM {self.model.table} where {self.model.table}.id in (select {f_col} from {mtm} where {m_col} = {model.id})"

            db.cursor.execute(sql)
             data = db.cursor.fetchall()

         return [self._loadWithLogic(r) for r in data] if data else None
 
     def insert_relation(self, model, mtm, m_col, f_col):
         with DataBaseConnection() as db:
             db.cursor.execute(
                f"INSERT INTO {mtm} ({m_col}, {f_col}) VALUES ({self.model.id}, {model.id})"
             )
 
     def delete_relation(self, model, mtm, m_col, f_col):
         with DataBaseConnection() as db:
             db.cursor.execute(
                f"DELETE FROM {mtm} WHERE {m_col} = '{self.model.id}' AND {f_col} = '{model.id}'"
             )