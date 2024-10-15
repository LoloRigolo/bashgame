## Test for command people

# Import
from commands import people

def test_init():
    # Test people -list : name1 is a Blacksmith because of test_blacksmith
    assert people.run(["-list"]) == {"Names": ["name1", "name2", "name3"], "Jobs": ["Blacksmith", "free", "free"]}
    old_name, new_job = "name2", "Lumberjack"
    assert people.run(["-assign", old_name, new_job]) == f"{old_name} is now a {new_job}" # Assign name2 to a Lumberjack
    assert people.run(["-list"]) == {"Names": ["name1", old_name, "name3"], "Jobs": ["Blacksmith", new_job, "free"]}
    new_name = "test_name"
    assert people.run(["-rename", old_name, new_name]) == f"{old_name} succefully rename to {new_name}" # Rename name2 to test_name
    assert people.run(["-list"]) == {"Names": ["name1", new_name, "name3"], "Jobs": ["Blacksmith", new_job, "free"]}

def test_people_error():
    assert people.run([]) == ["people", "OPTION","This command affect our people", { # Test of a no prompt
    "-list": "This command shows you a list of peoples!",
    "-rename" : "This command rename a people",
    "-assign" : "This command assign a job to a people"}]
    new_name, new_job = "test_name", "LumberJack",
    assert people.run(["-rename", new_name, new_name]) == "It's already the case" # Rename to the same
    assert people.run(["-assign", new_job, new_job]) == "It's already the case" # Assign to the same
    # 0 prompt
    assert people.run(["-rename"]) == ["people", "-rename OLDNAME NEWNAME", "This command rename a people"]
    assert people.run(["-assign"]) == ["people", "-assign NAME JOB", "This command assign a job to a people"]
    # Bad new_name
    bad_new_name = "name7"
    assert people.run(["-assign", new_name, bad_new_name]) == ["people", "-assign NAME JOB", "This command assign a job to a people"]

