         Close the database connection.
         """
         self.logger.info("Closing database connection.")
        self.connection.close()
        self.logger.info("Database connection closed.")
\ No newline at end of file