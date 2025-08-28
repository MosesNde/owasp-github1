     Session = sessionmaker(bind=engine)
     session = Session()
 
    # deal with SQL injections
    name = '%s' % search_name
 
     try:
        states = session.query(State).filter(State.name.like(f'%{name}%')).first()
         if states:
             print(states.id)
         else: