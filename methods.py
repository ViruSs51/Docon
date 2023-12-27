from dataclasses import dataclass
from typing import Callable
import asyncio

import exceptions

@dataclass
class LoopData:
    function_draw: Callable[[], None]
    begin: bool
    
class Loop:
    
    def __init__(self,
                 function_draw: Callable[[], None],
                 begin: bool=True
                 ) -> None:
        self.loop: LoopData = LoopData(
            function_draw=function_draw,
            begin=begin
            )
    
    async def start(self
                    ) -> None:
        while self.loop.begin:
            await self.loop.function_draw()
            await asyncio.sleep(0.00000001)
    
    async def set(self,
            key: str,
            value: any
            ) -> None:
        if key in self.loop.__dict__:
            self.loop.__dict__[key] = value
        else:
            raise exceptions.LoopKeyError