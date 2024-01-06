#Main exceptions
class ErrorApplication(Exception):
    '''Main - exception'''

    def __init__(self, 
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Global: Fatal error'
    
    def __str__(self
                ) -> str:
        return self.message
    
 
#Loop exceptions
class LoopError(ErrorApplication):
    '''Loop main - exception class'''

    def __init__(self, 
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Loop: Fatal error'

class LoopSetError(LoopError):
    '''Loop set new value - exception class'''
    
    def __init__(self, 
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Set: Fatal error'

class LoopSetKeyError(LoopSetError):
    '''Loop key set - exception class'''

    def __init__(self, 
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Set key: Fatal error'


#Hasher exceptions
class HasherError(ErrorApplication):
    '''Hasher - exception class'''

    def __init__(self,
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Hasher: Fatal error'

class HasherKeyError(HasherError):
    '''Hasher key - exception class'''

    def __init__(self,
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Key: Fatal error'

class HasherKeyGenerateError(HasherKeyError):
    '''Hasher key generate - exception class'''

    def __init__(self,
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Key generate: Fatal error'

class HasherKeyGenerateCharLengthError(HasherKeyGenerateError):
    '''Char length - exception class'''

    def __init__(self,
                 *args
                 ) -> None:
        self.message = args[0] if args else 'The length indicated for a character is wrong'

class HasherKeyNameError(HasherKeyError):
    '''Key name - exception class'''

    def __init__(self,
               *args
               ) -> None:
        self.message = args[0] if args else 'Key name: Fatal error'