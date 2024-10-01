# Test for wait command

from commands import wait

def test_init():
    response = wait.run([]) # Test 0 input
    assert response == ["wait", "OPTION","This command advance the time", {"-hour":"Advance the time to X:int hour(s)","-day":"Advance the time to X:int day(s)"}]
    response = wait.run(["-day"]) # Test "-day" input
    assert response == ["wait", "-day NUMBER_OF_DAYS:int", "Advance the time to X:int day(s)"]
    response = wait.run(["-hour"]) # Test "-hour" input
    assert response == ["wait", "-hour NUMBER_OF_HOURS:int", "Advance the time to X:int hour(s)"]

