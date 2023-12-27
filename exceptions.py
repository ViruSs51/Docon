class Error(Exception):
    '''Main exception'''

    def __init__(self, 
                 *args
                 ) -> None:
        self.message = args[0] if args else None
    
    def __str__(self
                ) -> None:
        message = self.message

        if self.__class__ == Error:
            message = 'Global: Fatal error'

        elif self.__class__ == LoopError:
            message = 'Loop: Fatal error'
        
        elif self.__class__ == LoopSetError:
            message = 'Set: Fatal error' 
        
        elif self.__class__ == LoopKeyError:
            message =  'Key do not exit'

        return message if self.message is None else self.message

class LoopError(Error):
    '''Loop main exception class'''

class LoopSetError(LoopError):
    '''Set new value exception class'''

class LoopKeyError(LoopSetError):
    '''Key exception class'''
