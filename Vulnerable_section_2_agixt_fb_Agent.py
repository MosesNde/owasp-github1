             json.dump(self.AGENT_CONFIG, f)
 
     def get_commands_string(self):
         if len(self.available_commands) == 0:
            return None

         enabled_commands = filter(
             lambda command: command.get("enabled", True), self.available_commands
         )
         if not enabled_commands:
            return None

         friendly_names = map(
            lambda command: f"`{command['friendly_name']}` - Arguments: {command['args']}",
             enabled_commands,
         )
         if not friendly_names:
             return ""
        command_list = "\n".join(friendly_names)
        return f"Commands Available To Complete Task:\n{command_list}\n\n"
 
     def get_provider(self):
         config_file = self.get_agent_config()