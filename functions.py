#In this file is a simple function

def delete_char(string: str, 
                char: str
                ) -> str:
    try:
        index_char = string.index(char)
    except ValueError:
        return string
    
    return string[:index_char] + string[index_char+1:]