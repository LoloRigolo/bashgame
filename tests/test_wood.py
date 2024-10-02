#Test for object wood

import pytest
from environmental_variables import Wood

@pytest.fixture()
def wood():
    return Wood() # Init wood at 0

def test_init(wood: Wood):
    assert wood.get() == 0 # Verif if wood = 0

def test_update_wood(wood: Wood):
    wood.update(50) # Update wood + 50, wood = 50
    assert wood.get() == 50
    wood.update(-25) # Update wood + 25, wood = 25
    assert wood.get() == 25

