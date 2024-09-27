# Library
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.console import Console

from commands import helloworld
from commands import wait

# Functions
def options_panel(command_carac:list) -> list:
    # Function to create the help of any command
    text = Text()
    text.append(f"{command_carac[0]} {command_carac[1]}\n", style = "pink")
    text.append(f"{command_carac[2]}", style="pink")
    panel_desc = Panel(text, title = f"{command_carac[0]} help", border_style="magenta")
    if len(command_carac) > 3:
        table = Table()
        table.add_column("option", justify = "left", no_wrap=True)
        table.add_column("description", justify = "left")
        for key in command_carac[3].keys():
            table.add_row(key,command_carac[3][key])
        panel_table = Panel(table, border_style="magenta")
        Console().print(panel_table)
        return [panel_desc,panel_table]
    return [panel_desc]

def run(user_input:str):
    # Function to run commands
    user_input.lower()
    user_input:list = user_input.split()
    text_response = Text()

    # Command helloworld
    if user_input[0] == "helloworld":
        helloworld_response = helloworld.helloworld(user_input[1:])
        if  isinstance(helloworld_response, list):
            return options_panel(helloworld_response)
        text_response.append(helloworld_response, style = "green")

    #Command wait
    elif user_input[0] == "wait":
        wait_response = wait.wait(user_input[1:])
        if  isinstance(wait_response, list):
            return options_panel(wait_response)
        text_response.append(wait_response, style = "green")

    else:
        text_response.append("Invalid Syntax", style = "red")

    return [text_response]

