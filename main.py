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
from hub.packages import Packages
from colors.colors import Colors
"""
Primary execution point of the applicatino.

The CLI data is read in
"""
def main():
    # Instantiate the CLI class object and acquire the data passed in from the CLI at program runtime.
    cli = CLI()
    args = cli.return_given_arguments()
    csv = CsvParser()

    parsed_packages = csv.parse_packages_csv()
    distance_table = csv.parse_distance_table_data_dump_into_hash()
    packages = Packages(parsed_packages)

    trucks = Trucks(parsed_packages)

    print(f"{Colors.OKGREEN}All deliveries were completed with total mileage of: {trucks.total_distance}{Colors.ENDC}")
    if args.all:
        packages.print_all_packages()
    elif args.package:
        print(parsed_packages.get(int(args.package)))
    elif args.time:
        packages.all_packages_with_timestamp(args.time)

if __name__ == '__main__':
    main()
