import asyncio

import commands
import methods

class Docon(commands.Command):

    def __init__(self,
                 interface: bool=False
                 ) -> None:
        self.interface = interface
    
    async def run(self
                  ) -> None:
        self.loop = methods.Loop(
            function_draw=self.draw_window if self.interface else self.draw_terminal,
            begin=True
            )

        await asyncio.gather(self.loop.start())
    
    async def draw_terminal(self
                   ) -> None:
        command = input('<Docon>: ').split()
        command_length = len(command)

        if command:
            output = ''

            if command[0] == 'exit' and command_length == 1:
                await self.exit(loop=self.loop)
            
            elif command[0] == 'help':
                if command_length == 1:
                    output = await self.help()
                
                elif command_length == 2:
                    output = await self.help(command=command[1])
                
                else:
                    output = f'[{command[0]}] parameters are not correct {command[2:]}'
            
            elif command[0] == 'new':
                if command_length == 3:
                    output = await self.new(parameters=command[1:])

                else:
                    output = f'The [{command[0]}] command is not entered correctly'
            
            else:
                output = f'This command [{command[0]}] does not exist'

            print(f'{output}\n')
        
    async def draw_window(self
                          ) -> None:
        pass

if __name__ == '__main__':
    app = Docon()
    asyncio.run(app.run())