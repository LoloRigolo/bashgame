#Test for object hour

import pytest
import environmental_variables as ev

@pytest.fixture()
def hour():
    return ev.Hour()# Init hour at 1


def test_init(hour: ev.Hour):
    assert hour.get() == 1 # verif of fixture

def test_hour_update(hour: ev.Hour):
    hour.update(5) # update hour + 5 = 6
    assert hour.get() == 6

