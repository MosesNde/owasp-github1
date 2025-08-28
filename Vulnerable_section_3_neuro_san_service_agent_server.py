         current_dir = os.path.dirname(os.path.abspath(__file__))
 
         setup_logging(SERVER_NAME_FOR_LOGS, current_dir,
                      'DECISION_ASSISTANT_SERVICE_LOG_JSON',
                      'DECISION_ASSISTANT_SERVICE_LOG_LEVEL')
         # This module within openai library can be quite chatty w/rt http requests
         logging.getLogger("httpx").setLevel(logging.WARNING)
 