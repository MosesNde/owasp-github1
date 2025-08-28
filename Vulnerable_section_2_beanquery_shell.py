 
     def do_output(self, arg):
         """Send output to FILE or stdout if FILE is omitted."""
        self.outfile = open(arg, "w") if arg else sys.stdout
 
     def do_parse(self, arg):
         """Run the parser on the following command and print the output."""