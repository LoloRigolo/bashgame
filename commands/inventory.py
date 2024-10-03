# Import 
from environmental_variables import wood_instance, metal_instance

def run(options:list):
    # Run the command if it's not possible call description
    if len(options) == 0:
        wood, metal  = wood_instance.get(), metal_instance.get()
        return {"object":["wood","metal"], "quantity":[str(wood), str(metal)]}
    else :
        return description()

def description():
    return ["inventory", "NO-OPTIONS", "Show your inventory"]
