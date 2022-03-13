from hub.csv_parser import CsvParser
from formulas.formulas import Formulas
from datetime import timedelta, datetime

"""
Routing Algorithm objects for providing optimal routes
"""


class RoutingAlgorithm:
    """
    Constructor for RoutingAlgorithm
    O(1)
    """
    def __init__(self, packages):
        self.packages = packages
        self.distance_data, self.address_headers = CsvParser().parse_distance_table_data_dump_into_hash()

    """
    Sorts delivery data for set of packages, determines shortest paths between vertices of a "grpah" of noddes.
    Updates the packages with delivered timestmaps and tracks the distance of the truck.
    Tracks total mileage to be returned to as to set yhe mileage for the truck.
    
    The algorithm here is an implementation of the "nearest neighbor" algorithm to determine the next route based off of
    all routes in the arrays of times. Which can be thought of as vertices of graph. Given our current location in euclidean space, we
    determine the next smallest value from all vertices that we have in our addresses.
    
    O(N^2)
    """
    def sort_fastest_routes(self, truck, return_to_hub=False):
        addresses_array = []
        {addresses_array.append({key: value}) for (key, value) in self.distance_data.items() for node in self.packages if
         node.delivery_street_address == key}
        addresses = {key:value for (key, value) in self.distance_data.items() for node in self.packages if node.delivery_street_address == key}
        address_vertices = [vertices for vertices in addresses.values()]
        packages_already_delivered = []

        address_count = len(addresses_array) - 1
        ticker = 0

        for p in self.packages:
            address_data = addresses[p.delivery_street_address]
            # Update first package with distance from hub and deliver it.
            if ticker == 0:
                self.update_package_and_truck(truck, p, address_data[0])
                ticker += 1
                continue

            if return_to_hub and ticker == address_count:
                # Begin and end at hub
                self.update_package_and_truck(truck, p, address_data[0])
                continue

            # HERE: some truck3 items are broken and showing 2 AM lol
            neighbors = self.get_nearest_addresses(address_vertices, address_data, 2)
            for i in range(len(self.packages)):
                if list(addresses_array[i].values())[0] == neighbors:
                    if p.delivery_street_address in packages_already_delivered:
                        self.update_package_and_truck(truck, p,
                                                      self.find_distance_between_the_closest_element(neighbors, list(
                                                          addresses_array[i].items())[0][0]), True)
                    else:
                        packages_already_delivered.append(p.delivery_street_address)
                        self.update_package_and_truck(truck, p, self.find_distance_between_the_closest_element(neighbors, list(addresses_array[i].items())[0][0]))

            ticker += 1

    """
    Primary engine behind the algorithm for determining shortest path.
    O(N)
    """
    def get_nearest_addresses(self, address_vertices, row, neighbors_count):
        distances = list()
        for r in address_vertices:
            dist = Formulas().euclidean_distance(row, r)
            distances.append((r, dist))
        distances.sort(key=lambda tup: tup[1])
        neighbors = list()
        for i in range(neighbors_count):
            neighbors.append(distances[i][0])
        # only ever return the first neighbor as this is the next node we will visit.
        # Return the distance value itself for time calculation and the nearest neighbors array
        return neighbors[1]

    """
    Update package data fields
    O(1)
    """
    def update_package_and_truck(self, truck, package, distance, already_ran=False):
        hour = truck.delivery_time.split(":")[0]
        minute = truck.delivery_time.split(":")[1].split(" ")[0]
        delivery_time = (datetime(100, 1, 1, int(hour), int(minute)) +
                         timedelta(minutes=Formulas().get_time_from_distance_and_speed(distance, 18))).strftime("%I:%M %p")
        package.delivery_status = 'delivered'
        package.package_time = delivery_time
        truck.delivery_time = delivery_time
        if already_ran is False:
            truck.total_miles += distance

    """
    Determine the exact distance between addresses
    O(N)
    """
    def find_distance_between_the_closest_element(self, neighbors, key):
        for i in range(len(self.address_headers)):
            if self.address_headers[i] == key:
                return neighbors[i-1]
