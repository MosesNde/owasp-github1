             command for command in agent_commands if agent_commands[command] == True
         ]
         for command in available_commands:
            verbose_commands += f'    "{command["friendly_name"]}": {{\n'
             for arg in command["args"]:
                 verbose_commands += f'        "{arg}": "Your hallucinated input",\n'
             verbose_commands += "    },\n"