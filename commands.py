from types import FunctionType

import methods
import exceptions


class CommandAnswer: 

    async def command_not_entered_correctly(self,
                                            command_name: str
                                            ) -> str:
        commands_list = [c 
                         for c in dir(Command) 
                         if isinstance(getattr(Command, c), FunctionType)
                         ]

        return f'The [{command_name}] command is not entered correctly' + (f'\n\nFor usage information type - help {command_name}' if command_name in commands_list else '')

    async def command_parameters_not_correct(self,
                                             command: list,
                                             start_incorrect_index: int=1
                                             ) -> str:
        return f'[{command[0]}] parameters are not correct {command[start_incorrect_index:]}\n\nFor usage information type - help {command[0]}'

class Command(CommandAnswer):
    
    async def exit(self,
                   loop: methods.Loop
                   ) -> None:
        '''Closing the program cycle'''
        await loop.set(
            key='begin', 
            value=False
            )
    
    async def help(self,
                   command: str|None=None
                   ) -> str:
        '''Display all available commands and their usage explanations'''
        commands_list = [c 
                         for c in dir(Command) 
                         if isinstance(getattr(Command, c), FunctionType)
                         ]
        commands_list.remove('help')

        if command:
            if command in commands_list:
                return f' {command}: {getattr(Command, command).__doc__}'
            
            else:
                return await self.command_not_entered_correctly(command_name=command)
        else:
            commands_documentation = '\n\n'.join([
                f' {c}: {getattr(Command, c).__doc__}' 
                for c in commands_list
                ])

        return f'''\nCommands list:\n{commands_documentation}'''
    
    async def new(self,
                  command: tuple|list
                  ) -> str:
        '''
    Using:
        new <object-type> [parameters]

    Object types:
        - hash-key: Generate a key for the hasher and save it
          
            Parameters:
                - key-name: The name for the key that can be used to access it in the '''
        hasher = methods.Hasher()
        
        if command[1] == 'hash-key':
            try:
                return await hasher.generate_key(key_name=command[2])
            
            except exceptions.HasherKeyNameError as err:
                return err

        else:
            return await self.command_parameters_not_correct(command=command)