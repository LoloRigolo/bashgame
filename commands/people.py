# people.py
import environmental_variables as EnvVar
import utilites_functions as uf

people = EnvVar.people_instance

# People class to manage people

# OPTIONS and description for the function related to people
OPTIONS: dict = {
    "-set": "This command creates new people!",
    "-list": "This command shows you a list of people!"
}



def run(options: list):
    if len(options) == 0:
        return description()
    elif options[0] in OPTIONS:
        if options[0] == "-list" and len(options) == 1:
            # List all people
            return people.people_list
        return description(options[0])

# The description function to show details about commands related to people
def description(command_option:str = "") -> list:
    # Show the description of the command or of this parameters's description
    if command_option == "-set":
        wait_description_text: list= ["people", "-set NAME WORK",OPTIONS[command_option]]
    else:
        wait_description_text: list = ["people", "OPTION","This command affect our people",OPTIONS]
    return wait_description_text

