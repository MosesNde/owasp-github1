 
         with self.lock:
             self.cur.execute(
                "INSERT INTO bridge (room_id, channel_id) "
                f"VALUES ('{room_id}', '{channel_id}')"
             )
             self.conn.commit()
 
     def add_user(self, mxid: str) -> None:
         with self.lock:
            self.cur.execute(f"INSERT INTO users (mxid) VALUES ('{mxid}')")
             self.conn.commit()
 
     def add_avatar(self, avatar_url: str, mxid: str) -> None:
         with self.lock:
             self.cur.execute(
                f"UPDATE users SET avatar_url = '{avatar_url}'"
                f"WHERE mxid = '{mxid}'"
             )
             self.conn.commit()
 
     def add_username(self, username: str, mxid: str) -> None:
         with self.lock:
             self.cur.execute(
                f"UPDATE users SET username = '{username}'"
                f"WHERE mxid = '{mxid}'"
             )
             self.conn.commit()
 