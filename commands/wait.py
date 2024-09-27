# import
import environmental_variables as EnvVar

def wait(options:list) -> list:
    if len(options) == 1:
        return wait_description(options[0])
    elif len(options) > 1:
        if options[0] in {"-hour"}:
            EnvVar.hour_instance.update_hour(int(options[1]))
            return f"Advance the time during {options[1]} hour(s)"
        elif options[0] in {"-day"}:
            EnvVar.day_instance.update_day(int(options[1]))
            return f"Advance the time during {options[1]} day(s)"
    else:
        return wait_description()

def wait_description(command_option = ""):
    OPTIONS: dict = {"-hour":"Advance the time to X hour(s)","-day":"Advance the time to X day(s)"}
    if command_option == "-hour":
        wait_description_text: list= ["wait", "-hour NUMBER_OF_HOURS",OPTIONS[command_option]]
    elif command_option == "-day":
        wait_description_text: list= ["wait", "-day NUMBER_OF_DAYS",OPTIONS[command_option]]
    else:
        wait_description_text: list = ["wait", "OPTION","This command advance the time",OPTIONS]
    return wait_description_text