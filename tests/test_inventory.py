# Test for command

from commands import inventory
from environmental_variables import wood_instance, metal_instance

def test_init():
    response = inventory.run(["inventory test"]) # invalid input
    assert response == ["inventory", "NO-OPTIONS", "Show your inventory"]

def test_inventory():
    wood = wood_instance.get() # Verif wood_instance
    assert wood == 0
    metal  = metal_instance.get() # Verif metal_instance
    assert metal == 0
    response = inventory.run([]) # Verif with a correct input
    assert response == {"object":["wood","metal"], "quantity":[str(wood), str(metal)]}