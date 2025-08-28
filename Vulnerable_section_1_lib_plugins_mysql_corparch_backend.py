                 'GROUP BY c.name '
                 'HAVING num_match_keys >= %s ) '
                 'UNION ').format(where1=' AND '.join('(' + wc + ')' for wc in where_cond1))
        where.extend(values_cond2)
         total_acc_sql, total_acc_args = self._total_access_query(user_id)
         where.extend(total_acc_args)
         sql += (
             '(SELECT c.name as id, c.web, '
             'IF (rc.locale IS NOT NULL, rc.locale, c.collator_locale) as collator_locale, '