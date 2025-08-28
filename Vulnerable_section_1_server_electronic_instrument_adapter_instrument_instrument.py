         command_type = self.commands_map[command_base]['type']
 
         # Inject command parameters
        self.__generate_command_with_injected_params(command)
 
         if command_type == COMMAND_TYPE_SET:
             written_bytes = self.device.write(self.commands_map[command_base]['command'])