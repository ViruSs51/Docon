from os import listdir
from random import choice
from types import FunctionType

from dataclasses import dataclass
import asyncio

import exceptions

def delete_char(string: str, char: str):
    try:
        index_char = string.index(char)
    except ValueError:
        return string
    
    return string[:index_char] + string[index_char+1:]

@dataclass
class LoopData:
    function_draw: FunctionType
    begin: bool
    
class Loop:
    
    def __init__(self,
                 function_draw: FunctionType,
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
            await asyncio.sleep(0.000000000000000000001)
    
    async def set(self,
            key: str,
            value: any
            ) -> None:
        if key in self.loop.__dict__:
            self.loop.__dict__[key] = value

        else:
            raise exceptions.LoopKeyError

@dataclass  
class HashData:
    characters: str
    separator: str
    character_lenght: int
    key: list|str

class Hasher:

    def __init__(self,
                 characters: str='1234567890!@#$%^&*()-=_+`~,./;\'[]\\<>?:"}{|qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM',
                 separator: str='|'
                 ) -> None:
        self.data = HashData(
            characters=characters,
            separator=separator,
            character_lenght=3,
            key=[]
            )
    
    async def generate_key(self,
                           key_name: str,
                           character_length: int=3
                           ) -> None:
        self.data.character_lenght = character_length

        characters_not_separator = delete_char(self.data.characters, self.data.separator)
        for c in self.data.characters:
            while True:
                new_character = ''.join(
                    [choice(characters_not_separator) 
                     for i in range(self.data.character_lenght)
                     ])
                
                if new_character not in self.data.key:
                    break

            self.data.key.append(new_character)
            
        self.data.key = f'{self.data.character_lenght}{self.data.separator}{"".join(self.data.key)}'

        key_not_exist = True
        if 'docon-key-data.dcs' in listdir():
            with open('docon-key-data.dcs', 'r') as docon_file:
                for key in docon_file.read().split('\n'):
                    if key.split(self.data.separator)[0] == key_name:
                        break

                else: 
                    key_not_exist = False
        else:
            key_not_exist = False

        if key_not_exist:
            return f'The name [{key_name}] for the key already exists'

        else:
            with open('docon-key-data.dcs', 'a') as docon_file:
                docon_file.write(f'{key_name}{self.data.separator}{self.data.key}\n')
                
            return 'The key was created successfully'