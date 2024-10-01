# Test for command Helloworld

from commands import helloworld

def test_init():
    response = helloworld.run([]) # Test 0 input
    assert response == "Hello, World!"
    response = helloworld.run(["-name", "Name"]) #Test "-name Name" in imput
    assert response == "Hello, Name!"
    response = helloworld.run(["-help"]) # Test "something" in input
    assert response == ["helloworld", "OPTION","This command tell you hello !", {"-name":"This command tell you hello !"}]
    response = helloworld.run(["-name"]) # Test "-name" in input
    assert response == ["helloworld", "-name YOURNAME","This command tell you hello !"]
    response = helloworld.run(["-test", "lolo"]) # Test "something something" in input
    assert response == ["helloworld", "OPTION","This command tell you hello !", {"-name":"This command tell you hello !"}]
