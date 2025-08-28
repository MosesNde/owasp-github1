 import time
 import json
 from analyzer.PI_detection import VULPIXAnalyzer
from tester.exceptions import TimeOutError, VULPIXAnalyzerError, ExternalInterfaceError, PaidAppError, resolve_exit_code
 from interfaces.external import ExternalOutputInterface
 import logging
 
 TIMEOUT_SEC = 5 * 60
     else:
         result_interface = ExternalOutputInterface()
 
     cmd = [
         'python3',
         './monkey.py',