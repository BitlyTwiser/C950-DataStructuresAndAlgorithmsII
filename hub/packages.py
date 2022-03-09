# Tracks all the packages and updates accordingly
class Packages:
    def __init__(self, package_id, delivery_address, delivery_deadline, package_mass, special_notes):
        self.package_Id = package_id
        self.delivery_address = delivery_address
        self.delivery_deadline = delivery_deadline
        self.package_mass = package_mass
        self.special_notes = special_notes

