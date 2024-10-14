# Test for command blacksmith

# Import
from commands import blacksmith, people


def test_init():
    assert blacksmith.run(["-list"]) == "No blacksmiths in activty !" # At begining nothing
    people.run(["-assign", "name1", "Blacksmith"]) # Make name1 a Blacksmith and verif if listed
    assert blacksmith.run(["-list"]) == {"Blacksmiths": ["name1"], "Level": ["No more forge buildings available"], "Productions": ["No production"]}

def test_command_error():
    #Tests errors
    assert blacksmith.run([]) == ["blacksmith", "OPTION","With this command you can manage blacksmiths", {"-list": "Show blacksmiths, their levels and production"}]
    assert blacksmith.run(["-list",""]) == ["blacksmith", "-list", "Show blacksmiths, their levels and production"]