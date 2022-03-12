from hub.csv_parser import CsvParser

"""
Routing Algorithm objects for providing optimal routes
"""


class RoutingAlgorithm:
    def __init__(self, packages):
        self.packages = packages
        self.distance_data = CsvParser().parse_distance_table_data_dump_into_hash()

    def sort_fastest_routes(self):
        self.packages
