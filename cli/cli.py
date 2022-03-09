import argparse


# CLI class object for the user interface
# Simple argparse user interface
class CLI:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-a', '--all', action='store_true',
                            help='Displays data for ALL packages')
        self.parser.add_argument('-p', '--p', type=str,
                            help='Displays data for specific package using provided package ID')
        self.parser.add_argument('-t', '--time', type=str,
                            help='Displays Data for ALL packages based on the input time interval. Input must be in military time. i.e. 13:00')

    # Returns the arguments provided via the cli interface
    def return_given_arguments(self):
        return self.parser.parse_args()
