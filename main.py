#########################
# Name: Joshua Groeschl #
# Student Id: 01133572  #
#########################


# Make item that ingest csv data and loads it into the application
# create custom hash table
# create CLI and way to interface with application
#
from cli.cli import CLI
from structures.hashtable import HashMap
from hub.csv_parser import CsvParser


def main():
    # Instantiate the CLI class object and aquire the data passed in from the CLI at program runtime.
    cli = CLI()
    args = cli.return_given_arguments()

    packages = CsvParser().parse_packages_csv()

    if (args.all):
        packages.print_all()

if __name__ == '__main__':
    main()
