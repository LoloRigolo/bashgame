#Test for object metal

import pytest
from environmental_variables import Metal

@pytest.fixture()
def metal():
    return Metal() # Init metal at 0

def test_init(metal: Metal):
    assert metal.get() == 0 # Verif if metal = 0

def test_update_metal(metal: Metal):
    metal.update(50) # Update metal + 50, metal = 50
    assert metal.get() == 50
    metal.update(-25) # Update metal + 25, metal = 25
    assert metal.get() == 25
