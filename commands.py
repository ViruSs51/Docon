from types import FunctionType

import methods

class Command:
    
    async def exit(self,
                   loop: methods.Loop
                   ) -> None:
        '''Closing the program cycle'''
        await loop.set(
            key='begin', 
            value=False
            )
        
        quit()
    
    async def help(self,
                   command: str|None=None
                   ) -> str:
        '''Get commands list and commands description'''
        commands_list = [c 
                         for c in dir(Command) 
                         if isinstance(getattr(Command, c), FunctionType)
                         ]
        commands_list.remove('help')

        if command:
            if command in commands_list:
                return f' {command}: {getattr(Command, command).__doc__}'
            
            else:
                return f'This [{command}] command does not exist'
        else:
            commands_documentation = '\n\n'.join([
                f' {c}: {getattr(Command, c).__doc__}' 
                for c in commands_list
                ])

        return f'''\nCommands list:\n{commands_documentation}'''
    
    async def new(self,
                  parameters: tuple
                  ) -> None:
        '''
    Using:
        new <object-name> [parameters]

    parameter list:
        * hash-key: Create key for encryption and decryption of information
          new hash-key <key-name>'''
        hasher = methods.Hasher()
        
        if parameters[0] == 'hash-key':
            return await hasher.generate_key(key_name=parameters[1])

        else:
            return f'Parameters are not correct [{parameters}]'