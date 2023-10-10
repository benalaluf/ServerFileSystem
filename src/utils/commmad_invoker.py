
class CommandInvoker:
    def __init__(self, commands: dict):
        self.commands = commands

    def exec(self, command: str):
        if command:
            command = command.split(' ')
            command_parms = command[1:]

            func = self.commands.get(command[0])

            if func:
                if command_parms:
                    func(command[1])
                else:
                    func()
            elif command[0] == "help":
                self.__print_available_commands()
            else:
                print(f'{command} is unknown, try "help"')

    def __print_available_commands(self):
        print("The available commands are: ")
        for command in self.commands:
            print(f'- "{command}"')
