#########################
# Name: Joshua Groeschl #
# Student Id: 01133572  #
#########################


from cli.cli import CLI
from structures.hashtable import HashMap
from hub.csv_parser import CsvParser
from hub.trucks import Trucks
from hub.packages import Packages
from colors.colors import Colors
from formulas.formulas import Formulas
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
    # Tuple unpacking for packages hash and list.
    packages_hash, parsed_packages = csv.parse_packages_csv()
    packages = Packages(parsed_packages)

    trucks = Trucks(packages_hash)
    # Tuple unpacking to grab all trucks.
    t1, t2, t3 = trucks.truck_loading_dock()

    # Run all the deliveries, then just use the timestamps to parse the data and determine what has been delivered and waht has not been
    # Adjust the reports accordingly.
    # We will use delivery time for this, if the given timestamp is before the item is delivered its at the hub
    # If its before the truck itself leaves, then its at hub lol
    # Run all deliveries
    trucks.run_deliveries(t1, t2, t3)

    if args.all:
        packages.print_all_packages()
        trucks.print_delivery_message()
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
                # Note: Do the same check here for departure time and delivery time before displaying results
                # This one is easy as its a single package.
                # Run all the things, check deliver time and the truck departure time.
                # at this time we have delivered everythuing, now we just hack the time items to show to client
                # When we get this to work for a single item, we can do it for all.
                # if time we want >= truck.departure and package.delivery is not none and >= time we want
                # Display as is, else if time < truck.departure, its at hug
                # else if time > departure < delivery is None, its in transite.
                trucks.print_delivery_message()
                Formulas().package_data_display_engine_for_specific_time(package_by_id, timestamp)
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
            # Fix it here
            for package in packages.packages:
                if package is None:
                    continue
                else:
                    Formulas().package_data_display_engine_for_start_and_end_time(package, start_time_timestamp,
                                                                                  end_time_timestamp)

            packages.print_all_packages()
            trucks.print_delivery_message()


if __name__ == '__main__':
    main()
