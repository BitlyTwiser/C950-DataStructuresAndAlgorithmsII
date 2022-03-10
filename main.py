#########################
# Name: Joshua Groeschl #
# Student Id: 01133572  #
#########################


# Make item that ingest csv data and loads it into the application
# create custom hash table
# create CLI and way to interface with application

from cli.cli import CLI
from structures.hashtable import HashMap
from hub.csv_parser import CsvParser
from hub.trucks import Trucks

"""
Primary execution point of the applicatino.

The CLI data is read in
"""
def main():
    # Instantiate the CLI class object and acquire the data passed in from the CLI at program runtime.
    cli = CLI()
    args = cli.return_given_arguments()
    csv = CsvParser()

    packages = csv.parse_packages_csv()
    distance_table = csv.parse_distance_table_data_dump_into_hash()
    trucks = Trucks(packages)

    print(f"All deliveries were completed with total mileage of: {trucks.total_distance}")
    if (args.all):
        packages.print_all()

if __name__ == '__main__':
    main()
