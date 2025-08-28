         curs.execute('CREATE TABLE test (x int)')
         curs.executemany('INSERT INTO test VALUES (?)', [(i, ) for i in range(16)])
 
 
 class TestBeanquery(APITests, unittest.TestCase):
     @classmethod