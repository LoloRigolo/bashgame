# Library
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.console import Console

from commands import helloworld, people, wait

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


##coder la fonction table_panel renvoie une liste de liste coder un panel ... avec les info qui a dans people response 

def table_panel(dico: dict):
    table = Table()
    values = list(dico.values())
    for key in dico:
        table.add_column(key, justify= "left")
    for pair in zip(*values):
        table.add_row(pair[0],pair[1])
    panel_table = Panel(table, border_style="blue")
    return [panel_table]

def run(user_input:str):
    # Function to run commands
    user_input.lower()
    user_input:list = user_input.split()
    text_response = Text()

    # Command helloworld
    if user_input[0] == "helloworld":
        helloworld_response = helloworld.run(user_input[1:])
        if  isinstance(helloworld_response, list):
            return options_panel(helloworld_response)
        text_response.append(helloworld_response, style = "green")

    #Command wait
    elif user_input[0] == "wait":
        wait_response = wait.run(user_input[1:])
        if  isinstance(wait_response, list):
            return options_panel(wait_response)
        text_response.append(wait_response, style = "green")
    
    elif user_input[0] == "people":
        people_response = people.run(user_input[1:])
        if  isinstance(people_response, list):
            return options_panel(people_response)
        elif isinstance(people_response, dict):
            return table_panel(people_response)
        text_response.append(people_response, style = "green")
        

    else:
        text_response.append("Invalid Syntax", style = "red")

    return [text_response]

