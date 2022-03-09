import argparse


# CLI class object for the user interface
# Simple argparse user interface
class CLI:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-a', '--all', action='store_true',
                            help='Displays data for ALL packages')
        self.parser.add_argument('-p', '--package', type=str,
                            help='Displays Data for Specific package')

    # Returns the arguments provided via the cli interface
    def return_given_arguments(self):
        return self.parser.parse_args()
