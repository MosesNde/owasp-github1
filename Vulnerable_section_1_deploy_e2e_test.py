         engine = create_engine(DATABASE_DSN)
         with engine.connect() as connection:
             for trade in self.test_trades:
                connection.execute(text(f"""DELETE FROM "trades" WHERE id = '{trade.id}';"""))
             connection.commit()
            # logger.info("Trade Delete")
     def tearDown(self) -> None:
         self._delete_trades()  
 