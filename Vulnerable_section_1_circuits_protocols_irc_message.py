 class Message(object):
 
     def __init__(self, command, *args, **kwargs):
        for arg in args[:-1]:
            if u(" ") in arg:
                raise Error("Space can only appear in the very last arg")
 
         self.command = command
        self.args = list(filter(lambda x: x is not None, list(args)))
         self.prefix = text_type(kwargs["prefix"]) if "prefix" in kwargs else None
 
         self.encoding = kwargs.get("encoding", "utf-8")
 
     def __unicode__(self):
         args = self.args[:]
        for arg in args[:-1]:
            if arg is not None and u(" ") in arg:
                raise Error("Space can only appear in the very last arg")
 
        if len(args) > 0 and u(" ") in args[-1] and args[-1][0] != u(":"):
             args[-1] = u(":{0:s}").format(args[-1])
 
         return u("{prefix:s}{command:s} {args:s}\r\n").format(