                 chformatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
             else:
                 chformatter = logging.Formatter('%(message)s')
             # add formatter to handler
             fhandler.setFormatter(fhformatter)
             #fhandler.setLevel(logging.DEBUG)