from math import sqrt
import datetime

class Formulas:
    """
    Returns time taken for the distance traveled.
    O(1)
    """

    def get_time_from_distance_and_speed(self, distance, speed):
        return (distance / speed) * 60

    """
    Determines how to adjust packages to display correct data upon the user input query for time range.
    O(N)
    """

    def package_data_display_engine_for_start_and_end_time(self, package, start_time, end_time):
        package = package.value
        package_departure_time = package.package_truck_departure_time
        if start_time < package_departure_time:
            package.delivery_status = "at hub"
            package.package_time = "None"
        elif start_time >= package_departure_time <= end_time and start_time >= package.package_time <= end_time and package.delivery_status != 'delivered':
            package.delivery_status = 'en route'
            package.package_time = "None"
        elif start_time >= package_departure_time and (end_time < package.package_time or package.delivery_status != 'delivered'):
            package.delivery_status = 'en route'
            package.package_time = "None"

    """
    Determines how to adjust packages to display correct data upon the user input query for specific time.
    O(N)
    """

    def package_data_display_engine_for_specific_time(self, package, start_time):
        package_departure_time = package.package_truck_departure_time
        if package.package_Id == "9" and start_time < datetime.time(hour=10, minute=21).strftime("%I:%M %p"):
            package.delivery_address = '300 State St, Salt Lake City, UT, 84103'
        if start_time <= package_departure_time:
            package.delivery_status = "at hub"
            package.package_time = "None"
        elif start_time >= package_departure_time and start_time >= package.package_time:
            pass
        elif start_time >= package_departure_time < package.package_time:
            package.delivery_status = 'en route'
            package.package_time = "None"
    """
    Calculates euclidean distance between two vertices
    O(N)
    """
    def euclidean_distance(self, row1, row2):
        distance = 0.0
        for i in range(len(row1) - 1):
            distance += (row1[i] - row2[i]) ** 2
        return sqrt(distance)

