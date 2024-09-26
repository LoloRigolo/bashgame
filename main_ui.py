# UI player in a terminal app

# Library
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

# Importation
import commands

# Vars
console = Console()
golds = 100
day = 1
times = [1,"00"]

# Functions
def info(current_day,current_times,current_golds):
    # Function to display the info
    info_text = Text()
    info_text.append(f"Day: {current_day}\n")
    info_text.append(f"Time: {current_times[0]}h{current_times[1]}\n")
    info_text.append(f"Golds: {current_golds}", style = "Yellow")
    info_panel = Panel(info_text, title = "INFO", border_style = "bold cyan", width = 20)
    return  console.print(info_panel, justify = "left")

def term(response = [""]):
    # The Terminal app
    console.clear()
    info(day, times, golds)
    if response[0] != "":
        if isinstance(response[0],list):
            for i in range (len(response[0])):
                console.print(response[0][i])
        else:
            console.print(response[0])

    command = input("> ")
    if command == "quit":
        console.print(Text("Goodbye !", style = "green"))
        return 
    elif command == "":
        term()
    elif commands.test_input(command):
        term(commands.run(command)) #call an python file where commands are save
    else:
        term([Text("Invalid syntax", style = "red")])

term()
