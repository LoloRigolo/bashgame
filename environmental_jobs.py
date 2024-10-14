## Environmental_job file
# Here we create jobs object and instance them

# JOBS dispo
JOBS = ["Blacksmith","Lumberjack","free"]

# Import
from environmental_variables import people_instance

# Production Var
TIER_1_PROD = "1/h"
TIER_2_PROD = "3/h"
TIER_3_PROD = "5/h"

#Blacksmith Job
class Blacksmith:

    def __init__(self) -> None:
        pass

    def level(self) -> list:
        # Without builds purpose no set the level
        level: list = []
        for people in people_instance.blacksmith():
            level.append("No more forge buildings available")
        return level
    
    def production(self) -> list:
        # Show the production in function of the level
        production: list = []
        levels: list = self.level()
        for level in levels:
            if level == "Tier-1":
                production.append(f"{TIER_1_PROD} metal")
            elif level == "Tier-1":
                production.append(f"{TIER_1_PROD} metals")
            elif level == "Tier-3":
                production.append(f"{TIER_3_PROD} metals")
            else:
                production.append("No production")
        return production

    def blacksmith_list(self) -> dict:
        # Return a dict of blacksmiths and thier levels
        bs_list: dict = {"Blacksmiths": people_instance.blacksmith(), "Level": self.level(), "Productions": self.production()}
        return bs_list

    def get_len_list(self) -> int:
        # Return a the number(int) of blacksmith
        bs_list: dict = self.blacksmith_list()
        return len(bs_list["Blacksmiths"])
    
    


## Instances 
# jobs
blacksmith_job = Blacksmith()