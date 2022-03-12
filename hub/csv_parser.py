import csv
from hub.packages import Package
from structures.hashtable import HashMap
import datetime
import base64

"""
Parses the CSV data from the CSV files to initially load into the hashtable
O(1) time complexity
"""
def parse_address_from_csv_data(address, city, state, zipcode):
    return f"{address}, {city},{state} {zipcode}"


class CsvParser:
    def __init__(self):
        self.packages_csv = 'wgups_package_file.csv'
        self.distance_table_csv = 'wgups_distance_table.csv'

    # Private helper method to parse address from fields.
    """
    Parse distance table data and create hash containing vertices of the distance values and keys of base64 
    encoded address strings.  
    We also create a list from the csv header values denoting each address as a 
    lookup table for when we determine route paths
    O(N)
    """
    def parse_distance_table_data_dump_into_hash(self):
        distance_table = {}
        distance_csv_array = []
        with open(self.distance_table_csv) as distance_csv:
            csv_data = csv.reader(distance_csv, delimiter=',')
            initial_row_array = next(csv_data)[2:]
            initial_row_array = [ base64.b64encode(address.split("\n", 2)[1].replace(",", "").strip().encode("ascii")) for address in initial_row_array ]

            for row in csv_data:
                distance_table[base64.b64encode(row[0].split("\n", 2)[1].replace(",", "").strip().encode("ascii"))] = [float(r) if r != "" else 0 for r in row[2:]]
                #distance_table[row[0].split("\n", 2)[1].replace(",", "").strip()] = row[2:]

        return distance_table, initial_row_array
    """
    Parses packages CSV and stores data into custom hash table
    O(N)
    """
    def parse_packages_csv(self):
        packages_hash = HashMap()
        with open(self.packages_csv) as packages_csv:
            csv_data = csv.reader(packages_csv, delimiter=',')
            next(csv_data)  # Skip header
            for row in csv_data:
                # Build address from fields in csv
                address = parse_address_from_csv_data(row[1], row[2], row[3], row[4])

                # Other fields
                package_id = row[0]
                delivery_deadline = row[5]
                mass = row[6]
                special_notes = row[7]

                # All packages start at hub
                package = Package(
                    package_id,
                    address,
                    delivery_deadline,
                    mass,
                    special_notes,
                    "at the hub",
                    datetime.time(hour=8, minute=0).strftime("%I:%M %p"),
                    base64.b64encode(row[1].strip().encode("ascii"))
                    #row[1]
                )

                packages_hash.add(int(package_id), package)

        return packages_hash, packages_hash.buckets
