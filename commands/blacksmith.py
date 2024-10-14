# Blacksmith.py

# Import
from environmental_jobs import blacksmith_job

# Options of blacksmith command
OPTIONS: dict = {
    "-list": "Show blacksmiths, their levels and production"
    }

def run(options: list):
    if len(options) == 0:
        return description()
    elif options[0] == "-list" and len(options) == 1:
        if blacksmith_job.get_len_list() == 0:
            return "No blacksmiths in activty !"
        return blacksmith_job.blacksmith_list()
    return description(options[0])


def description(command_option:str = "") -> list:
    # Show the description of the command or of this parameters's descriptions
    if command_option == "-list":
        helloworld_description_text: list= ["blacksmith", "-list", OPTIONS[command_option]]
    else:
        helloworld_description_text: list = ["blacksmith", "OPTION","With this command you can manage blacksmiths",OPTIONS]
    return helloworld_description_text
