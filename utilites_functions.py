# Utilities functions

def to_int(string:str) -> bool:
    # Verif if a string can be a an int
    try:
        int(string)
        return True
    except ValueError:
        return False