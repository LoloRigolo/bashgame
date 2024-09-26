# Library
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

# Vars

COMMANDS = { # stockage of commands in a dico { command_name:{ options:{ option1:desc of option1, option2:desc of option2 }, "description":desc of command_name } }
            "helloworld":{"options":
                            {"-name":"to add your name after hello"}
                        ,"description":"This command tell you hello !"}
            }

# Functions
def options_panel(key:str, command_carac:str) -> list:
    # Function to create the help of any command
    text = Text()
    text.append(f"{key} {command_carac}\n", style = "pink")
    text.append(f"{COMMANDS[key]["description"]}", style="pink")
    table = Table()
    table.add_column("option", justify = "left", no_wrap=True)
    table.add_column("description", justify = "right")
    for option in COMMANDS[key]["options"]:
        table.add_row(option,COMMANDS[key]["options"][option])
    panel_desc = Panel(text, title = f"{key} help", border_style="magenta")
    panel_table = Panel(table, border_style="magenta")
    return [panel_desc,panel_table]

def hello_world(option1:str,option2:str="") -> list:
    # Function to tell you hello with option
    if option1 != False:
        if option1 in COMMANDS["helloworld"]["options"]:
          if option1 == "-name":
            hello_world_text = Text(f"Hello {option2} !", style="green")
        else:
            return [options_panel("helloworld","OPTION")]
    else:
        hello_world_text = Text("Hello world !", style="green")
    return [hello_world_text]

def run(user_input:str):
    # Function to run commands
    user_input.lower()
    user_input:list = user_input.split()
    user_input.append(False)
    user_input.append(False)
    if user_input[0] in {"helloworld"}:
        return hello_world(user_input[1],user_input[2])

def test_input(user_input:str,commands:dict=COMMANDS) -> bool:
    # Function to check if the user_input is a command
    user_input.lower()
    user_input:list = user_input.split()
    if user_input[0] in commands.keys():
        return True
    return False

options_panel("helloworld","OPTION")