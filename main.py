import asyncio

import commands
import methods

class Docon(commands.Command):
    
    async def run(self,
            interface: bool=True
            ) -> None:
        self.interface = interface
        self.loop = methods.Loop(
            function_draw=self.draw,
            begin=True
            )
        
        await asyncio.gather(self.loop.start())
    
    async def draw(self
             ) -> None:
        command = input('>>> ').split()

        if command != []:
            if command[0] == 'exit':
                await self.exit(self.loop)

if __name__ == '__main__':
    app = Docon()
    asyncio.run(app.run())