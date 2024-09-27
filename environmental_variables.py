## environmental_variable file


# Day object
class Day:
    def __init__(self, day=1):
        self.day = day

    def get_day(self) -> int:
        return self.day
    
    def update_day(self, increment:int) -> int:
        self.day += increment
        return self.day

# Hour object
class Hour:
    def __init__(self, hour=1):
        self.hour = hour
    
    def get_hour(self) -> int:
        return self.hour
    
    def update_hour(self, increment:int) -> int:
        self.hour += increment
        return self.hour

# Gold object
class Gold:
    def __init__(self, gold=100):
        self.gold = gold
    
    def get_gold(self) -> int:
        return self.gold
    
    def update_gold(self, increment:int) -> int:
        self.gold += increment
        return self.gold


# Instances init
day_instance = Day()
hour_instance = Hour()
gold_instance = Gold()