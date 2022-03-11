import datetime
from hub.csv_parser import CsvParser

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
        self.distance_table_data = CsvParser().parse_distance_table_data_dump_into_hash()
        # The new value for the known bad address for package #9.
        self.new_address = '410 S State St., Salt Lake City, UT 84111'

    def truck_loading_dock(self):
        truck1_packages = [
            self.packages[1],
            self.packages[13],
            self.packages[14],
            self.packages[15],
            self.packages[16],
            self.packages[17],
            self.packages[19],
            self.packages[20],
            self.packages[21],
            self.packages[29],
            self.packages[30],
            self.packages[31],
            self.packages[34]
        ]
        truck2_packages = [
            self.packages[3],
            self.packages[6],
            self.packages[18],
            self.packages[25],
            self.packages[26],
            self.packages[28],
            self.packages[32],
            self.packages[33],
            self.packages[36],
            self.packages[37],
            self.packages[38],
            self.packages[40],
        ]
        self.packages[9].value.delivery_address = self.new_address
        truck3_packages = [
            self.packages[2],
            self.packages[4],
            self.packages[5],
            self.packages[7],
            self.packages[8],
            self.packages[9],
            self.packages[10],
            self.packages[11],
            self.packages[12],
            self.packages[22],
            self.packages[23],
            self.packages[24],
            self.packages[27],
            self.packages[35],
            self.packages[39],
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
        return Truck3(truck3_packages, self.truck3_departure)

    """
    Determines total mileage of all trucks traveled
    O(1)    
    """

    def calculate_total_mileage(self, truck1_mileage, truck2_mileage, truck3_mileage):
        self.total_distance = (truck1_mileage + truck2_mileage + truck3_mileage)

        return self.total_distance

    """
    Determines the final delivery timestamp
    O(1)
    """

    def calculate_final_delivery_time(self, truck1_time, truck2_time, truck3_time):
        pass

    """
    Performs all deliveries and utilizes the algorithms for optimal routing of all packages within each truck.
    """

    def run_deliveries(self, truck1, truck2, truck3):
        self.distance_table_data
        truck1.start_deliveries()
        truck2.start_deliveries()
        truck3.start_deliveries()


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

    """
    Sets time value as deliveries are made.
    O(1)
    """

    def set_time(self, time):
        self.departure_time + time

    def package_delivery(self):
        pass

    # Keep track of arbitrary time value here. Upon delivery also update the tie value so thae CLI programwill pick it up.
    def start_deliveries(self):
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
        self.time = departure_time

    """
    Sets time value as deliveries are made.
    O(1)
    """

    def set_time(self, time):
        self.departure_time + time

    def package_delivery(self):
        pass

    def start_deliveries(self):
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
        self.time = departure_time

    """
    Sets time value as deliveries are made.
    O(1)
    """

    def set_time(self, time):
        self.departure_time + time

    def package_delivery(self):
        pass

    def start_deliveries(self):
        pass
