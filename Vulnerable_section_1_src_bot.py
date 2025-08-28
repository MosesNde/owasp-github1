 
     # bot.py, at the bottom of event_message
     if message.startswith("!"):
        message = message[:message.index(";")]
         split_msg = message.strip('!').split(' ')
         cmd = split_msg[0]
         args = split_msg[1:] if len(split_msg) > 0 else None