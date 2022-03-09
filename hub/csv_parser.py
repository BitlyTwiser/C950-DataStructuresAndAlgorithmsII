import csv
from hub.packages import Packages
from structures.hashtable import HashMap


# Parses the CSV data from the CSV files to initially load into the hashtable
def parse_address_from_csv_data(address, city, state, zipcode):
    return f"{address}, {city},{state} {zipcode}"


class CsvParser:
    def __init__(self):
        self.packages_csv = 'wgups_package_file.csv'
        self.distance_table_csv = 'wgups_distance_table.csv'

    # Private helper method to parse address from fields.

    def parse_distance_table_data_dump_into_hash(self):
        with open(self.distance_table_csv) as distance_csv:
            csv_data = csv.reader(distance_csv, delimiter=',')
            next(csv_data)  # Skip header

            for row in csv_data:
                # Build address from fields in csv
                address = parse_address_from_csv_data(row[1], row[2], row[3], row[4])

                # Other fields
                package_id = row[0]
                delivery_deadline = row[5]
                mass = row[6]
                special_notes = row[7]

                package = Packages(package_id, address, delivery_deadline, mass, special_notes)

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

                package = Packages(package_id, address, delivery_deadline, mass, special_notes, "at the hub")
                packages_hash.add(package_id, package)

        return packages_hash
