from os import listdir
from random import choice
from types import FunctionType

from dataclasses import dataclass
import asyncio

import functions
import exceptions


@dataclass
class LoopData:
    function_draw: FunctionType
    begin: bool
    
class Loop:
    
    def __init__(self,
                 function_draw: FunctionType|tuple[FunctionType],
                 begin: bool=True
                 ) -> None:
        '''Cycle initialization to program'''
        self.__loop: LoopData = LoopData(
            function_draw=function_draw,
            begin=begin
            )
    
    async def start(self
                    ) -> None:
        while self.__loop.begin:
            await self.__loop.function_draw()
            await asyncio.sleep(0.000000000000000000001)
    
    async def set(self,
            key: str,
            value: any
            ) -> None:
        '''Set new parameters for loop constant'''
        if key in self.__loop.__dict__:
            self.__loop.__dict__[key] = value

        else:
            raise exceptions.LoopSetKeyError('Key don\'t exit in loop data')


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
        self.__data = HashData(
            characters=characters,
            separator=separator,
            character_lenght=None,
            key=[]
            )
    
    async def generate_key(self,
                           key_name: str,
                           character_length: int=3
                           ) -> None:
        if character_length > 0:
            self.__data.character_lenght = character_length
        
        else:
            raise exceptions.HasherKeyGenerateCharLengthError

        characters_not_separator = functions.delete_char(self.__data.characters, self.__data.separator)
        for c in self.__data.characters:
            while True:
                new_character = ''.join(
                    [choice(characters_not_separator) 
                     for i in range(self.__data.character_lenght)
                     ])
                
                if new_character not in self.__data.key:
                    break

            self.__data.key.append(new_character)
            
        self.__data.key = f'{self.__data.character_lenght}{self.__data.separator}{"".join(self.__data.key)}'

        key_not_exist = True
        if 'docon-key-data.dcs' in listdir():
            with open('docon-key-data.dcs', 'r') as docon_file:
                for key in docon_file.read().split('\n'):
                    if key.split(self.__data.separator)[0] == key_name:
                        break

                else: 
                    key_not_exist = False
        else:
            key_not_exist = False

        if key_not_exist:
            raise exceptions.HasherKeyNameError(f'The name [{key_name}] for the key already exists')

        else:
            with open('docon-key-data.dcs', 'a') as docon_file:
                docon_file.write(f'{key_name}{self.__data.separator}{self.__data.key}\n')
                
            return 'The key was created successfully'