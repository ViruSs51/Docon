import methods

class Command:
    
    async def exit(self,
             loop: methods.Loop
             ) -> None:
        await loop.set(
            key='begiwn', 
            value=False
            )