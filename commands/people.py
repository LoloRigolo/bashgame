# people.py

#import
from environmental_variables import people_instance
import environmental_jobs as ej
from utilites_functions import regex_name

people = people_instance

# OPTIONS and description for the function related to people
OPTIONS: dict = {
    "-list": "This command shows you a list of peoples!",
    "-rename" : "This command rename a people",
    "-assign" : "This command assign a job to a people"
}

def run(options: list):
    if len(options) == 0:
        return description()
    elif options[0] in OPTIONS:
        if options[0] == "-list" and len(options) == 1:
            return people.people_list
        elif options[1] == options[2] or people.get_job(options[1]) == options[2]:
            return "It's already the case"
        elif options[0] == "-rename" and len(options) == 3 and regex_name(options[2]) and options[1] in people.people_list["Names"]:
            people.rename(options[1], options[2])
            return f"{options[1]} succefully rename to {options[2]}"
        elif options[0] == "-assign" and len(options) == 3 and options[2] in ej.JOBS and options[1] in people.people_list["Names"]:
            people.assign(options[1], options[2])
            return f"{options[1]} is now a {options[2]}"
        return description(options[0])

# The description function to show details about commands related to people
def description(command_option:str = "") -> list:
    # Show the description of the command or of this parameters's description
    if command_option == "-list":
        wait_description_text: list= ["people", "-list" ,OPTIONS[command_option]]
    elif command_option == "-rename":
        wait_description_text: list= ["people", "-rename OLDNAME NEWNAME" ,OPTIONS[command_option]]
    elif command_option == "-assign":
        wait_description_text: list= ["people", "-assign NAME JOB",OPTIONS[command_option]]
    else:
        wait_description_text: list = ["people", "OPTION","This command affect our people",OPTIONS]
    return wait_description_text

