def helloworld(kwargs):
    if len(kwargs) != 0:
        if len(kwargs) > 1:
            if kwargs[0] in {"-name"}:
                helloworld_text: str = f"Hello, {kwargs[1]}!"
        else:
            return helloworld_description(kwargs[0])
    else:
        helloworld_text: str = "Hello, World!"
    return helloworld_text

def helloworld_description(command_option) -> list:
    OPTIONS: dict = {"-name":"This command tell you hello !"}
    if command_option == "-name":
        helloworld_description_text: list= ["helloworld", "-name YOURNAME",OPTIONS[command_option]]
    else:
        helloworld_description_text: list = ["helloworld", "OPTION","This command tell you hello !",OPTIONS]
    return helloworld_description_text

