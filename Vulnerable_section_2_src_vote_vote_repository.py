         try:
             with psycopg2.connect(**self.config) as conn:
                 with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(f"""
                                 SELECT * 
                                 FROM public.stg_vote 
                                 WHERE vote_voting_external_id ='{voting_external_id}'
                                 """)
                     vote_rows : RealDictRow = cur.fetchall()
                     vote_list :list[Vote] =[VoteMapper.to_vote(vote_row) for vote_row in vote_rows]
         except (Exception, psycopg2.DatabaseError) as error:
         try:
             with psycopg2.connect(**self.config) as conn:
                 with conn.cursor(cursor_factory=RealDictCursor) as cur:
                    cur.execute(f"""
                                 SELECT * 
                                 FROM public.stg_vote 
                                 WHERE vote_voting_external_id IN ({vote_voting_external_id_list_str})
                                 """)
                     vote_rows : RealDictRow = cur.fetchall()
                     vote_list :list[Vote] =[VoteMapper.to_vote(vote_row) for vote_row in vote_rows]
         except (Exception, psycopg2.DatabaseError) as error: