import argparse


class CLI:
    def __init__(self) -> None:
        parser = argparse.ArgumentParser()
        parser.add_argument('-', '--', type=str,
                            help='')
        parser.add_argument('-', '--', type=int, default=3,
                            help='')
        parser.add_argument('-', '', type=bool, default=False,
                            help='')
