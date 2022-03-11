import datetime

"""
Packages Class Object

Sets package status upon delivery/departure
Sets time of packages based on distance traveled.
"""


class Package:
    def __init__(self, package_id, delivery_address, delivery_deadline, package_mass, special_notes, delivery_status,
                 package_time):
        self.package_Id = package_id
        self.delivery_address = delivery_address
        self.delivery_deadline = delivery_deadline
        self.package_mass = package_mass
        self.special_notes = special_notes
        self.delivery_status = delivery_status
        self.delivery_time = 'None'
        # separate time element to track just general time of package for the CLI interface
        self.package_time = package_time

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

    def set_package_time(self, package_time):
        self.package_time = package_time

    """
     Prints package details
     O(1)
    """

    def print_package_details(self):
        print(f"Package ID: {self.package_Id}\t"
              f"Address: {self.delivery_address}\t"
              f"Deadline: {self.delivery_deadline}\t "
              f"Mass: {self.package_mass}\t "
              f"Delivery Time: {self.delivery_time}\t"
              f"Status: {self.delivery_status}")


"""
Packages class for tracking ALL packages
"""


class Packages:
    """
        Constructor for Packages class
    """

    def __init__(self, packages):
        self.packages = packages

    """
     Finds all packages equal too given time range.
     O(1)
    """

    def all_packages_with_timestamp(self, timestamp):
        for index, element in enumerate(self.packages):
            node = self.packages[index]
            while node is not None:
                if element.value.package_time == timestamp:
                    element.value.print_package_details()
                    node = node.next
            if node is None:
                continue

        return

    """
     Finds all packages between given time ranges
     O(1)
    """

    def all_packages_in_time_range(self, start_time, end_time):
        for index, element in enumerate(self.packages):
            node = self.packages[index]
            while node is not None:
                if start_time <= element.value.package_time <= end_time:
                    element.value.print_package_details()
                node = node.next
            if node is None:
                continue

        return

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
