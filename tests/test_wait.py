# Test for wait command

from commands import wait
from environmental_variables import day_instance,hour_instance

def test_init():
    response = wait.run([]) # Test 0 input
    assert response == ["wait", "OPTION","This command advance the time", {"-hour":"Advance the time to X:int hour(s)","-day":"Advance the time to X:int day(s)"}]
    response = wait.run(["-day"]) # Test "-day" input
    assert response == ["wait", "-day NUMBER_OF_DAYS:int", "Advance the time to X:int day(s)"]
    response = wait.run(["-hour"]) # Test "-hour" input
    assert response == ["wait", "-hour NUMBER_OF_HOURS:int", "Advance the time to X:int hour(s)"]

def test_wait_hour():
    assert hour_instance.get() == 1 # Verif hour = 1
    response = wait.run(["-hour","5"]) # Test "-hour 5" input
    assert hour_instance.get() == 6
    assert response == "Advance the time during 5 hour(s)" # Test hour = 6

def test_wait_day():
    assert day_instance.get() == 1 # Verif day = 1
    response = wait.run(["-day", "5"]) # Test "-day 5" input
    assert day_instance.get() == 6
    assert response == "Advance the time during 5 day(s)" # Test day = 6

def test_wait_hour_and_day():
    response = wait.run(["-hour","32"]) # Test "-hour 32" input
    assert response == "Advance the time during 32 hour(s)"
    assert hour_instance.get() == 14
    assert day_instance.get() == 7 # Verif if hour = 14 and day = 7