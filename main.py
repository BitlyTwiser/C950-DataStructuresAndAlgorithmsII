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


def main():
  cli = CLI()
  args = cli.return_given_arguments()

  hash = HashMap()
  hash.add("Hello", 123123123)
  hash.add("Things", 123.123123)

  a = hash.get("Things")

  if(args.all):
    hash.print_all()

if __name__ == '__main__':
  main()