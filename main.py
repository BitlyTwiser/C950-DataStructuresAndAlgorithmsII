#########################
# Name: Joshua Groeschl #
# Student Id: 01133572  #
#########################


# Make item that ingest csv data and loads it into the application
# create custom hash table
# create CLI and way to interface with application
#
from structures.hashtable import HashMap


def main():
  hash = HashMap()
  hash.add("Hello", 123123123)
  hash.add("Things", 123.123123)
  hash.print_all()
  a = hash.get("Things")
  hash.print_all()


if __name__ == '__main__':
  main()