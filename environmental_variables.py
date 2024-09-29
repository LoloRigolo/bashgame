## environmental_variable file
#  Here we develop objects and instance them to use them everywhere

# Day object
class Day:
    def __init__(self, day = 1) -> int:
        # Init instance (default to 1)
        self.day = day

    def get(self) -> int:
        # Getter
        return self.day
    
    def update(self, increment:int) -> int:
        # Update with nbr (increment) given
        self.day += increment
        return self.day

# Hour object
class Hour:
    def __init__(self, hour=1) -> int:
        # Init instance (default to 1)
        self.hour = hour
    
    def next_days(self, increment:int):
        # Pass to next day if > 24
        while (increment + self.hour) >= 24:
            day_instance.update(1)
            increment = (increment + self.hour) - 24
            self.hour = 0
        self.hour += increment
        return self.hour

    def get(self) -> int:
        # Getteur
        return self.hour
    
    def update(self, increment:int):
        # Update with nbr (increment) given
        if (self.hour + increment) >= 24 :
            self.next_days(increment)
        else:
            self.hour += increment
        return self.hour

# Gold object
class Gold:
    def __init__(self, gold=100):
        # Init instance (default to 100)
        self.gold = gold
    
    def get(self) -> int:
        # Getter
        return self.gold
    
    def update(self, increment:int) -> int:
        # Update with nbr (increment) given
        self.gold += increment
        return self.gold


# Instances init
day_instance = Day()
hour_instance = Hour()
gold_instance = Gold()