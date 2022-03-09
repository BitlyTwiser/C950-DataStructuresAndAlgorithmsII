# Keeps track of all the truck movements
import datetime

# Truck 1 load with stuff and it goes out first, then comes back after the time of the faulty package and drivers switches
# to truck 3
# Truck 3 has all the packages that need to go out later and the package that has the faulty time that is corrected and does not come back
# truck 2 has everything else and never comes back
class Trucks:
    def __init__(self):
        # Truck one initially departs
        self.truck1_departure = datetime.time(hour=8, minute=0).strftime("%I:%M %p")
        # Truck 2 departs at the same time as truck 1
        self.truck2_departure = datetime.time(hour=8, minute=0).strftime("%I:%M %p")
        # 3rd truck departs AFTER the incorrect address was updated
        self.truck3_departure = datetime.time(hour=10, minute=21).strftime("%I:%M %p")

    def load_trucks(self):
        pass