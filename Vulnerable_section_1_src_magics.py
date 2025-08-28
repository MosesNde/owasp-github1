         population_id = bayesdb_get_population(self._bdb, population_name)
         table_name = bayesdb_population_table(self._bdb, population_id)
         table_name = table_name.encode('ascii','strict')
        raw_c = self._bdb.execute(
            '''SELECT * FROM %s;''' % (table_name,)) # TODO injection
         raw_df = utils_bql.cursor_to_df(raw_c)
         depprob_c = self._bdb.execute(
             '''SELECT name0, name1, value FROM
                (ESTIMATE DEPENDENCE PROBABILITY FROM PAIRWISE COLUMNS OF %s);''' % (population_name,)) # TODO injection
         depprob_df = utils_bql.cursor_to_df(depprob_c)
         schema = self._get_schema_as_list(population_name)
         return utils_plot.interactive_depprob(raw_df, depprob_df, schema)