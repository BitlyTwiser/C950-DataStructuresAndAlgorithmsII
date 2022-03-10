import datetime

# Truck 1 load with stuff and it goes out first, then comes back after the time of the faulty package and drivers switches
# to truck 3
# Truck 3 has all the packages that need to go out later and the package that has the faulty time that is corrected and does not come back
# truck 2 has everything else and never comes back
# All the trucks are separate objects, run the algorithm for delivery for each truck separately then report total time.
"""
Set status of packages to en route when they are loaded.
"""


class Trucks:
    def __init__(self, packages):
        self.packages = packages
        self.total_distance = 0
        self.truck1_departure = datetime.time(hour=8, minute=0).strftime("%I:%M %p")
        self.truck2_departure = datetime.time(hour=9, minute=5).strftime("%I:%M %p")
        self.truck3_departure = datetime.time(hour=10, minute=21).strftime("%I:%M %p")
        self.truck1_packages = []
        self.truck2_packages = []
        self.truck3_packages = []

    # Parses special notes and times to determine which trucks packages should be on.
    def truck_loading_dock(self, packages):
        pass

    def load_truck_one(self):
        pass

    def load_truck_two(self):
        pass

    def load_truck_three(self):
        pass

    def calculate_total_mileage(self):
        pass

    """
    Does all the delivering
    """

    def run_deliveries(self):
        pass


"""
Truck1 object, handles all deliveries and reporting for this truck
"""


class Truck1:
    # Constructor O(1)
    def __init__(self, packages, departure_time):
        self.packages = packages
        self.total_miles = 0
        self.departure_time = departure_time

    def package_delivery(self):
        pass


"""
Truck2 object, handles all deliveries and reporting for this truck
"""


class Truck2:
    # Constructor O(1)
    def __init__(self, packages, departure_time):
        self.packages = packages
        self.total_miles = 0
        self.departure_time = departure_time

    def package_delivery(self):
        pass


"""
Truck3 object, handles all deliveries and reporting for this truck
"""


class Truck3:
    # Constructor O(1)
    def __init__(self, packages, departure_time):
        self.packages = packages
        self.total_miles = 0
        self.departure_time = departure_time

    def package_delivery(self):
        pass
