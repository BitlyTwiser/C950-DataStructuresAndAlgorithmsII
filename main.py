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

    packages_hash, parsed_packages = csv.parse_packages_csv()
    packages = Packages(parsed_packages)

    trucks = Trucks(parsed_packages)
    # Tuple unpacking to grab all trucks.
    t1, t2, t3 = trucks.truck_loading_dock()

    print(f"{Colors.OKGREEN}All deliveries were completed with total mileage of: {Colors.BOLD}{Colors.OKBLUE}{trucks.total_distance}{Colors.ENDC}")
    if args.all:
        packages.print_all_packages()
    elif args.package:

        if args.time:
            try:
                package_id = int(args.package)
            except ValueError:
                print(f"{Colors.FAIL}You must pass in an integer for package ID!{Colors.ENDC}")
            else:
                package_by_id = packages_hash.get(package_id)
            try:
                split_time_string = args.time.split(":")
                timestamp = datetime.time(hour=int(split_time_string[0]), minute=int(split_time_string[1])).strftime(
                    "%I:%M %p")
            except IndexError:
                print(f"{Colors.FAIL}Please present time in format: HH:MM. Example: 16:00{Colors.ENDC}")
            else:
                if package_by_id.package_time >= timestamp:
                    package_by_id.print_package_details()
        else:
            print(f"{Colors.FAIL}One must use -t with the -p flag{Colors.ENDC}")
            return
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
