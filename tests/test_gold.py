#Test for object gold

import pytest
import environmental_variables as ev

@pytest.fixture()
def gold():
    return ev.Gold()# Init gold at 100


def test_init(gold: ev.Gold):
    assert gold.get() == 100 # verif of fixture

def test_update_gold(gold: ev.Gold):
    gold.update(54) # update gold + 54 = 154
    assert gold.get() == 154
