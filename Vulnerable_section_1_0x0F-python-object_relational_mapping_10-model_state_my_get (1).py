         else:
             print("Not found")
     except Exception as e:
        print(f"Error: {e}")
 '''
     # Construct the query with a bound parameter
     query = session.query(State).filter(State.name.like(':name'))