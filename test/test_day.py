#Test for object day
import pytest
import environmental_variables as ev

@pytest.fixture()
def day():
    return ev.Day()# Init dau at 1

def test_init(day: ev.Day):
    assert day.get() == 1 # verif of fixture

def test_day_update(day: ev.Day):
    day.update(54) # update day + 54 = 55
    assert day.get() == 55
