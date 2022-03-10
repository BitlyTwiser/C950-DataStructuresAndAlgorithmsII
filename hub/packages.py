import datetime
"""
Packages Class Object

Sets package status upon delivery/departure
Sets time of packages based on distance traveled.
"""


class Package:
    def __init__(self, package_id, delivery_address, delivery_deadline, package_mass, special_notes, delivery_status):
        self.package_Id = package_id
        self.delivery_address = delivery_address
        self.delivery_deadline = delivery_deadline
        self.package_mass = package_mass
        self.special_notes = special_notes
        self.delivery_status = delivery_status
        self.delivery_time = ''

    """
     Sets package status
     O(1)
    """

    def set_package_status(self, status):
        self.delivery_status = status

    """
     Sets package delivery Time
     O(1)
    """

    def set_package_delivery_time(self):
        pass

    def print_package_details(self):
        print(f"Package ID: {self.package_Id}\t"
              f"Address: {self.delivery_address}\t"
              f"Deadline: {self.delivery_deadline}\t "
              f"Mass: {self.package_mass}\t "
              f"Status: {self.delivery_status}")

"""
Packages class for tracking ALL packges
"""


class Packages:
    """
        Constructor for Packages class
    """

    def __init__(self, packages):
        self.packages = packages

    def all_packages_with_timestamp(self, timestamp):
        split_time_string = timestamp.split(":")

        return datetime.time(hour=int(split_time_string[0]), minute=int(split_time_string[1])).strftime("%I:%M %p")

    """
     Prints all elements from hashmap utilizing the linked list nodes to display values of elements.
     O(N^2)
    """
    def print_all_packages(self):
        for index, element in enumerate(self.packages):
            node = self.packages[index]
            while node is not None:
                element.value.print_package_details()
                node = node.next
            if node is None:
                continue
