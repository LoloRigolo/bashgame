# Utilities functions
import re

def regex_name(chaine):
    #verif a string not match NameInt
    pattern = r"^name\d+"
    return not re.match(pattern, chaine)

def to_int(string:str) -> bool:
    # Verif if a string can be a an int
    try:
        int(string)
        return True
    except ValueError:
        return False