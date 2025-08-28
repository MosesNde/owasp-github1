 
 @attr.define(kw_only=True)
 class ExtractCommandFailedReport(Report):
    """Describes an error when failed to run the exctraction command"""
 
     command: str
     stdout: bytes
     stderr: bytes
     exit_code: int