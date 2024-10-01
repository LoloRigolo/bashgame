# Options and description for the function
# {"-option" : "sa description"}
OPTIONS: dict = {"-name":"This command tell you hello !"}

def run(options: list):
    # Run the command if it's not possible call description
    if len(options) == 0:
         helloworld_text: str = "Hello, World!"
    elif len(options) == 1 or len(options) >= 3:
        return description(options[0])
    elif (options[0] in OPTIONS):
            if options[0] in {"-name"}:
                helloworld_text: str = f"Hello, {options[1]}!"
    else:
         return description()     
    return helloworld_text

def description(command_option:str = "") -> list:
    # Show the description of the command or of this parameters's descriptions
    if command_option == "-name":
        helloworld_description_text: list= ["helloworld", "-name YOURNAME",OPTIONS[command_option]]
    else:
        helloworld_description_text: list = ["helloworld", "OPTION","This command tell you hello !",OPTIONS]
    return helloworld_description_text

