import datetime
from colors.colors import Colors
from optimization.optimization import RoutingAlgorithm

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


    def truck_loading_dock(self):
        truck1_packages = [
            self.packages.get(15),
            self.packages.get(14),
            self.packages.get(16),
            self.packages.get(13),
            self.packages.get(1),
            self.packages.get(31),
            self.packages.get(30),
            self.packages.get(34),
            self.packages.get(20),
            self.packages.get(29),
            self.packages.get(17),
            self.packages.get(19),
            self.packages.get(21),
        ]
        truck2_packages = [
            self.packages.get(6),
            self.packages.get(3),
            self.packages.get(25),
            self.packages.get(40),
            self.packages.get(37),
            self.packages.get(18),
            self.packages.get(26),
            self.packages.get(28),
            self.packages.get(32),
            self.packages.get(33),
            self.packages.get(36),
            self.packages.get(38),
        ]
        truck3_packages = [
            self.packages.get(2),
            self.packages.get(4),
            self.packages.get(5),
            self.packages.get(7),
            self.packages.get(8),
            self.packages.get(9),
            self.packages.get(10),
            self.packages.get(11),
            self.packages.get(12),
            self.packages.get(22),
            self.packages.get(23),
            self.packages.get(24),
            self.packages.get(27),
            self.packages.get(35),
            self.packages.get(39),
        ]

        truck1 = self.load_truck_one(truck1_packages)
        truck2 = self.load_truck_two(truck2_packages)
        truck3 = self.load_truck_three(truck3_packages)

        return truck1, truck2, truck3

    """
    Loads truck 1 with packages
    """

    def load_truck_one(self, truck1_packages):
        return Truck1(truck1_packages, self.truck1_departure)

    """
    Loads truck 2 with packages
    """

    def load_truck_two(self, truck2_packages):
        return Truck2(truck2_packages, self.truck2_departure)

    """
    Loads truck 3 with packages and updates package #9 when we load truck 3
    """

    def load_truck_three(self, truck3_packages):
        # Do this when delivery starts

        return Truck3(truck3_packages, self.truck3_departure)

    """
    Determines total mileage of all trucks traveled
    O(1)    
    """

    def calculate_total_mileage(self, truck1_mileage, truck2_mileage, truck3_mileage):
        self.total_distance = (truck1_mileage + truck2_mileage + truck3_mileage)

    """
    Performs all deliveries and utilizes the algorithms for optimal routing of all packages within each truck.
    """

    def run_deliveries(self, truck1, truck2, truck3):
        truck1.start_deliveries()
        truck2.start_deliveries()
        truck3.start_deliveries()

        self.calculate_total_mileage(truck1.total_miles, truck2.total_miles, truck3.total_miles)

    def print_delivery_message(self):
        print(
            f"{Colors.OKGREEN}All deliveries were completed with total mileage of: {Colors.BOLD}{Colors.OKBLUE}{self.total_distance}{Colors.ENDC}")

"""
Truck1 object, handles all deliveries and reporting for this truck
"""


class Truck1:
    # Constructor O(1)
    def __init__(self, packages, departure_time):
        self.packages = packages
        self.total_miles = 0
        self.departure_time = departure_time
        self.time = departure_time
        # Used to track times of deliveries and when the truck needs to return to hub.
        self.delivery_time = departure_time

    """
    Sets the truck departure time of a package and status.
    O(N)
    """

    def set_time_and_initial_status_for_packages(self):
        for i in range(len(self.packages)):
            self.packages[i].package_truck_departure_time = self.departure_time
            self.packages[i].delivery_status = 'en route'

    # we only need a subset of the data from the distances CSV, anything that has the addresses we need here.
    # Aka split up the distances and do not use them all in each truck.
    def start_deliveries(self):
        self.set_time_and_initial_status_for_packages()
        algo = RoutingAlgorithm(self.packages)

        algo.sort_fastest_routes(self, return_to_hub=True)



"""
Truck2 object, handles all deliveries and reporting for this truck
"""


class Truck2:
    # Constructor O(1)
    def __init__(self, packages, departure_time):
        self.packages = packages
        self.total_miles = 0
        self.departure_time = departure_time
        self.time = departure_time
        self.delivery_time = departure_time

    """
    Sets the truck departure time of a package and status.
    O(N)
    """

    def set_time_and_initial_status_for_packages(self):
        for i in range(len(self.packages)):
            self.packages[i].package_truck_departure_time = self.departure_time
            self.packages[i].delivery_status = 'en route'

    # we only need a subset of the data from the distances CSV, anything that has the addresses we need here.
    def start_deliveries(self):
        self.set_time_and_initial_status_for_packages()
        algo = RoutingAlgorithm(self.packages)

        algo.sort_fastest_routes(self)



"""
Truck3 object, handles all deliveries and reporting for this truck
"""


class Truck3:
    # Constructor O(1)
    def __init__(self, packages, departure_time):
        self.packages = packages
        self.total_miles = 0
        self.departure_time = departure_time
        self.time = departure_time
        self.delivery_time = departure_time
        # The new value for the known bad address for package #9.
        self.new_address = '410 S State St., Salt Lake City, UT 84111'

    """
    Sets the truck departure time of a package and status.
    O(N)
    """

    def set_time_and_initial_status_for_packages(self):
        for i in range(len(self.packages)):
            self.packages[i].package_truck_departure_time = self.departure_time
            self.packages[i].delivery_status = 'en route'

    def start_deliveries(self):
        self.set_time_and_initial_status_for_packages()
        # Set good address for packages #9 since we now know the good address.
        self.packages[5].delivery_address = self.new_address
        algo = RoutingAlgorithm(self.packages)

        algo.sort_fastest_routes(self)
