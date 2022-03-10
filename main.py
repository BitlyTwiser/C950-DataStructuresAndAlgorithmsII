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
import datetime

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

    print(f"{Colors.OKGREEN}All deliveries were completed with total mileage of: {Colors.BOLD}{Colors.OKBLUE}{trucks.total_distance}{Colors.ENDC}")
    if args.all:
        packages.print_all_packages()
    elif args.package:
        try:
            package_id = int(args.package)
        except ValueError:
            print(f"{Colors.FAIL}You must pass in an integer!{Colors.ENDC}")
        else:
            print(parsed_packages.get(package_id))
    elif args.time:
        try:
            split_time_string = args.time.split(":")
            timestamp = datetime.time(hour=int(split_time_string[0]), minute=int(split_time_string[1])).strftime(
                "%I:%M %p")
        except IndexError:
            print(f"{Colors.FAIL}Please present time in format: HH:MM. Example: 16:00{Colors.ENDC}")
        else:
            packages.all_packages_with_timestamp(timestamp)
    elif args.timerange:
        try:
            start_time = args.timerange.split("-")[0].split(":")
            end_time = args.timerange.split("-")[1].split(":")
            start_time_timestamp = datetime.time(hour=int(start_time[0]), minute=int(start_time[1])).strftime(
                "%I:%M %p")
            end_time_timestamp = datetime.time(hour=int(end_time[0]), minute=int(end_time[1])).strftime(
                "%I:%M %p")
        except:
            print(f"{Colors.FAIL}Seems this is an invalid time value. Please present time in format: HH:MM-HH:MM. "
                  f"Example: 16:00-17:00{Colors.ENDC}")
        else:
            packages.all_packages_in_time_range(start_time_timestamp, end_time_timestamp)


if __name__ == '__main__':
    main()
