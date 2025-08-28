 
 import logging
 
from os import environ
 
 from argparse import ArgumentParser
 from pathlib import Path
                                 default=self.DEFAULT_TOOL_REGISTRY_FILE,
                                 help=".hocon or .json file defining the AgentToolRegistry for the service")
         arg_parser.add_argument("--port", type=int,
                                default=int(environ.get("DECISION_ASSISTANT_PORT",
                                                        AgentSession.DEFAULT_PORT)),
                                 help="Port number for the service")
 
         # Actually parse the args into class variables
         tool_registry: AgentToolRegistry = None
         tool_registry_file: str = args.tool_registry_file
         if tool_registry_file is not None and len(tool_registry_file) > 0:
             registry_name = Path(tool_registry_file).stem
             tool_registry = manifest_tool_registries.get(registry_name)
 
         logger.info("Shutdown: shutting down AsyncioExecutor")
         self.asyncio_executor.shutdown()
 
 
 if __name__ == '__main__':
     AgentMainLoop().main_loop()