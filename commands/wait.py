# Import
import environmental_variables as EnvVar
import utilites_functions as uf

# Options and description for the function
# {"-option" : "sa description"}
OPTIONS: dict = {"-hour":"Advance the time to X:int hour(s)","-day":"Advance the time to X:int day(s)"}


def run(options:list):
    # Run the command if it's not possible call description
    if len(options) == 0:
        return description()
    if len(options) == 1 or len(options) >= 3:
        return description(options[0])
    elif (options[0] in OPTIONS):
        if uf.to_int(options[1]):
            if options[0] in {"-hour"}:
                EnvVar.hour_instance.update(int(options[1]))
                return f"Advance the time during {options[1]} hour(s)"
            elif options[0] in {"-day"}:
                EnvVar.day_instance.update(int(options[1]))
                return f"Advance the time during {options[1]} day(s)"
        else:
            return description(options[0])
    
   

def description(command_option:str = "") -> list:
    # Show the description of the command or of this parameters's description
    if command_option == "-hour":
        wait_description_text: list= ["wait", "-hour NUMBER_OF_HOURS:int",OPTIONS[command_option]]
    elif command_option == "-day":
        wait_description_text: list= ["wait", "-day NUMBER_OF_DAYS:int",OPTIONS[command_option]]
    else:
        wait_description_text: list = ["wait", "OPTION","This command advance the time",OPTIONS]
    return wait_description_text