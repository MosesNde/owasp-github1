                 persona = self.agent.AGENT_CONFIG["settings"]["PERSONA"]
         if persona != "":
             persona = f"Your persona is: {persona}\n\n"
        verbose_commands = "**You have commands available to use if they would be useful to provide a better user experience.**\n```json\n{\n"
        agent_commands = self.agent.AGENT_CONFIG["commands"]
        # Get only the commands that are available to the agent, they're set to true in agent_commands. { "friendly name": true }
        available_commands = [
            command
            for command in agent_commands
            if str(agent_commands[command]).lower() == "true"
        ]
        for command in available_commands:
            verbose_commands += f'    "{command}": {{\n'
            command_args = Extensions(
                agent_name=self.agent_name,
                agent_config=self.agent.AGENT_CONFIG,
                ApiClient=self.ApiClient,
            ).get_command_args(command_name=command)
            for arg in command_args:
                verbose_commands += f'        "{arg}": "Your hallucinated input",\n'
            verbose_commands += "    },\n"
        verbose_commands += "}\n```"
        verbose_commands = '**To execute a command, use the example below, it will be replaced with the commands output for the user. You can execute a command anywhere in your response and the commands will be executed in the order you use them.**\n#execute_command("Name of Command", {"arg1": "val1", "arg2": "val2"})'
        if prompt_name == "Chat with Commands" and command_list == "":
             prompt_name = "Chat"
         file_contents = ""
         if "import_files" in prompt_args:
             string=prompt,
             user_input=user_input,
             agent_name=self.agent_name,
            COMMANDS=verbose_commands,
             context=context,
             command_list=command_list,
             date=datetime.now().strftime("%B %d, %Y %I:%M %p"),