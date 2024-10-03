# Import 
from environmental_variables import wood_instance, metal_instance

def run(options:list):
    # Run the command if it's not possible call description
    if len(options) == 0:
        return {"object":["wood","metal"], "quantity":[wood_instance.get(), metal_instance.get()]}
    else :
        return description()

def description():
    return ["inventory", "Show your inventory"]

