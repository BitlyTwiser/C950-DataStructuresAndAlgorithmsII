# Keeps track of all the truck movements
import datetime

# Truck 1 load with stuff and it goes out first, then comes back after the time of the faulty package and drivers switches
# to truck 3
# Truck 3 has all the packages that need to go out later and the package that has the faulty time that is corrected and does not come back
# truck 2 has everything else and never comes back
"""
Set status of packages to en route when they are loaded.
"""


class Trucks:
    def __init__(self, packages):
        self.packages = packages
        self.total_distance = 0
        self.truck1_mileage = 0
        self.truck2_mileage = 0
        self.truck3_mileage = 0
        # Truck one initially departs at 8 then arrives back at 10:20
        self.truck1_departure = datetime.time(hour=8, minute=0).strftime("%I:%M %p")
        # Truck 2 departs after delayed package arrive
        self.truck2_departure = datetime.time(hour=9, minute=5).strftime("%I:%M %p")
        # 3rd truck departs AFTER the incorrect address was updated and also accounts for all delayed packages WITHOUT a specific delivery time.
        # Update the address of the given truck at 10:20
        self.truck3_departure = datetime.time(hour=10, minute=21).strftime("%I:%M %p")
        self.truck1_packages = []
        self.truck2_packages = []
        self.truck3_packages = []
        # Call loading function in the constructor
        # self.truck_loading_dock(self.packages)

    # Parses special notes and times to determine which trucks packages should be on.
    def truck_loading_dock(self, packages):
        pass

    def load_truck_one(self):
        pass

    def load_truck_two(self):
        pass

    def load_truck_three(self):
        pass
