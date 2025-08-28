     PAID_APP_ERROR = 12
     ANALYZER_ERROR = 20
     EXTERNAL_INTERFACE_ERROR = 30
 
 class DynamicTestError(Exception):
     def __init__(self, message="Unexpected error while performing dynamic test"):
         self.exit_code = EXIT_CODE.EXTERNAL_INTERFACE_ERROR
         super().__init__(message)
 
 def resolve_exit_code(exit_code):
    return {
         EXIT_CODE.DYNAMIC_TEST_ERROR: DynamicTestError(),
         EXIT_CODE.TIMEOUT_ERROR: TimeOutError(),
         EXIT_CODE.PAID_APP_ERROR: PaidAppError(),
         EXIT_CODE.ANALYZER_ERROR: VULPIXAnalyzerError(),
         EXIT_CODE.EXTERNAL_INTERFACE_ERROR: ExternalInterfaceError(),
    }[exit_code]
\ No newline at end of file
\ No newline at end of file