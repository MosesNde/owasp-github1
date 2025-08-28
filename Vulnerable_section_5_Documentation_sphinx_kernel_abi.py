 import re
 import kernellog
 
from os import path

 from docutils import nodes, statemachine
 from docutils.statemachine import ViewList
 from docutils.parsers.rst import directives, Directive
     }
 
     def run(self):

         doc = self.state.document
         if not doc.settings.file_insertion_enabled:
             raise self.warning("docutils: file insertion disabled")
 
        env = doc.settings.env
        cwd = path.dirname(doc.current_source)
        cmd = "get_abi.pl rest --enable-lineno --dir "
        cmd += self.arguments[0]

        if 'rst' in self.options:
            cmd += " --rst-source"
 
        srctree = path.abspath(os.environ["srctree"])
 
        fname = cmd

        # extend PATH with $(srctree)/scripts
        path_env = os.pathsep.join([
            srctree + os.sep + "scripts",
            os.environ["PATH"]
        ])
        shell_env = os.environ.copy()
        shell_env["PATH"]    = path_env
        shell_env["srctree"] = srctree
 
        lines = self.runCmd(cmd, shell=True, cwd=cwd, env=shell_env)
         nodeList = self.nestedParse(lines, self.arguments[0])
         return nodeList
 
    def runCmd(self, cmd, **kwargs):
        u"""Run command ``cmd`` and return its stdout as unicode."""

        try:
            proc = subprocess.Popen(
                cmd
                , stdout = subprocess.PIPE
                , stderr = subprocess.PIPE
                , **kwargs
            )
            out, err = proc.communicate()

            out, err = codecs.decode(out, 'utf-8'), codecs.decode(err, 'utf-8')

            if proc.returncode != 0:
                raise self.severe(
                    u"command '%s' failed with return code %d"
                    % (cmd, proc.returncode)
                )
        except OSError as exc:
            raise self.severe(u"problems with '%s' directive: %s."
                              % (self.name, ErrorString(exc)))
        return out

     def nestedParse(self, lines, fname):
         env = self.state.document.settings.env
         content = ViewList()