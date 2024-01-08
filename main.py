import asyncio

import commands
import methods

class Docon(commands.Command, commands.CommandAnswer):

    def __init__(self,
                 interface: bool=False
                 ) -> None:
        self.interface = interface
    
    async def run(self
                  ) -> None:
        self.__loop = methods.Loop(
            function_draw=self.draw_window if self.interface else self.draw_terminal,
            begin=True
            )

        await asyncio.gather(self.__loop.start())
    
    async def draw_terminal(self
                   ) -> None:
        command = input('<Docon>: ').split()
        command_length = len(command)

        if command:
            output = ''

            if command[0] == 'exit' and command_length == 1:
                await self.exit(loop=self.__loop)
            
            elif command[0] == 'help':
                if command_length == 1:
                    output = await self.help()
                
                elif command_length == 2:
                    output = await self.help(command=command[1])
                
                else:
                    output = await self.command_parameters_not_correct(command=command, start_incorrect_index=2)
            
            elif command[0] == 'new':
                output = await self.new(command=command)
            
            else:
                output = await self.command_not_entered_correctly(command_name=command[0])

            if output: print(f'{output}\n')
        
    async def draw_window(self
                          ) -> None: ...

if __name__ == '__main__':
    app = Docon()
    asyncio.run(app.run())