class Error(Exception):
    '''Main exception'''

    def __init__(self, 
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Global: Fatal error'
    
    def __str__(self
                ) -> None:
        return self.message

class LoopError(Error):
    '''Loop main exception class'''

    def __init__(self, 
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Loop: Fatal error'

class LoopSetError(LoopError):
    '''Set new value exception class'''
    
    def __init__(self, 
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Set: Fatal error'

class LoopKeyError(LoopSetError):
    '''Key exception class'''

    def __init__(self, 
                 *args
                 ) -> None:
        self.message = args[0] if args else 'Key don\'t exit in loop data'