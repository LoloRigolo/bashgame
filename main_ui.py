# UI player in a terminal app

# Library
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

# Importation
from commands.utilites import function
import environmental_variables as EnvVar

# Vars
console = Console()


# Functions
def info(current_day,current_times,current_golds):
    # Function to display the info
    info_text = Text()
    info_text.append(f"Days: {current_day}\n")
    info_text.append(f"Hours: {current_times}h\n")
    info_text.append(f"Golds: {current_golds}", style = "Yellow")
    info_panel = Panel(info_text, title = "INFO", border_style = "bold cyan", width = 20)
    return  console.print(info_panel, justify = "left")

def term(response = [""]):
    # The Terminal app
    console.clear()
    info(EnvVar.day_instance.get(), EnvVar.hour_instance.get(), EnvVar.gold_instance.get())
    if response[0] != "":
        if isinstance(response,list):
            for i in range (len(response)):
                console.print(response[i])
        else:
            console.print(response)

    command = input("> ")
    if command in {"quit","q"}:
        console.print(Text("Goodbye !", style = "green"))
        return 
    elif command == "":
        term()
    else:
        term(function.run(command)) #call an python file where commands are save
term()
