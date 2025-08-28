         if persona != "":
             persona = f"Your persona is: {persona}\n\n"
         verbose_commands = "**You have commands available to use if they would be useful to provide a better user experience.**\n```json\n{\n"
        for command in self.agent.available_commands:
             verbose_commands += f'    "{command["friendly_name"]}": {{\n'
             for arg in command["args"]:
                 verbose_commands += f'        "{arg}": "Your hallucinated input",\n'