         try:
             with psycopg2.connect(**self.config) as conn:
                 with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(f"""
                                 SELECT * 
                                 FROM public.stg_voting 
                                 WHERE voting_id ='{voting_id}'
                                 ORDER BY voting_date DESC NULLS LAST
                                 LIMIT 100
                                 """)
                     voting_rows : RealDictRow = cur.fetchall()
                     voting_list :list[Voting] =[VotingMapper.to_voting(voting_row) for voting_row in voting_rows]
         ###TODO check if list is longer than 1
         try:
             with psycopg2.connect(**self.config) as conn:
                 with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(f"""
                                 SELECT * 
                                 FROM public.stg_voting 
                                 WHERE voting_affair_number ='{voting_affair_number}'
                                 ORDER BY voting_date DESC NULLS LAST
                                 LIMIT 100
                                 """)
                     voting_rows : RealDictRow = cur.fetchall()
                     voting_list :list[Voting] =[VotingMapper.to_voting(voting_row) for voting_row in voting_rows]
         except (Exception, psycopg2.DatabaseError) as error:
         try:
             with psycopg2.connect(**self.config) as conn:
                 with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(f"""
                                 SELECT * 
                                 FROM public.stg_voting 
                                 WHERE voting_body_key ='{voting_body_key}' AND
                                       voting_date >= '{min_date_string}' AND
									   voting_date <= '{max_date_string}'
                                 ORDER BY voting_date DESC NULLS LAST
                                 LIMIT {limit}
                                 """)
                     voting_rows : RealDictRow = cur.fetchall()
                     voting_list :list[Voting] =[VotingMapper.to_voting(voting_row) for voting_row in voting_rows]
         except (Exception, psycopg2.DatabaseError) as error: