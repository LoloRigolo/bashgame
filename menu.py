#
# Menu du jeu de LoloRigolo
#
# Main 0.1

# Library
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt


# Vars
USER = ""
TITRE = "-- Bash War --"

# Title
console = Console()
title = Text(TITRE, justify="center")
title.stylize("bold magenta", 0, len(title))
console.print(title, style="bold magenta", justify="center", width=console.width)

# Menu
def create_city(name_champ):
    console.print(f"What is the name of your city {name_champ}", style="green")
    name_city = input("Enter a city name : ")
    return name_city

def create_champ(name_champ):
    console.print("Hello stranger what is your name_champ ?", style="green")
    name_champ = console.input("Enter your name : ")
    console.print(f"So, hello {name_champ}", style="green")
    name_city = create_city(name_champ)
    return [ name_champ, name_city ]

def main_menu(name_champ):
    if name_champ == "" :
        name_champ = create_champ(name_champ)
    else:
        console.print(f"Welcome back {name_champ} !", style="green")
    return name_champ

USER = main_menu(USER)