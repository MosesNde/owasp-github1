     cols = [constants.COLUMN_NAMES[0]] + constants.COLUMN_NAMES[indices[0]:indices[1]]
     cols = ', '.join(cols)
     if suburbs:
        curs.execute(query % (cols, suburbs))
     else:
         curs.execute(query, (cols,))
     res = curs.fetchall()
     indices = testYears(startYear, endYear)
     if isinstance(indices, dict):
         return indices
    elif indices[0] == indices[1]:
         return {"Error": "Invalid start year", "Code": 400}
     if not isinstance(suburbs, list):
         suburbs = [suburbs]