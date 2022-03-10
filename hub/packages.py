"""
Packages Class Object

Sets package status upon delivery/departure
Sets time of packages based on distance traveled.
"""


class Packages:
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
