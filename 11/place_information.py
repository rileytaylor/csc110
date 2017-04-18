# This class stores information about a place. A place is composed of
# a name, address, tag(s), latitude and longitude. Latitude and longitude
# are stored as GeoLocation objects. This class also includes a method for
# finding the distance from this place to another GeoLocation.

from geolocation import *


class PlaceInformation:

    # constructs a place information object with given parameters
    def __init__(self, name, address, tag, latitude, longitude):
        self.__name = str(name)
        self.__address = str(address)
        self.__tag = str(tag)
        self.__latitude = float(latitude)
        self.__longitude = float(longitude)

    # returns the name of the place
    def get_name(self):
        return self.__name

    # returns the address of the place
    def get_address(self):
        return self.__address

    # returns the tag of the place
    def get_tag(self):
        return self.__tag

    # returns a string representation of the place
    def __str__(self):
        string = "name: " + str(self.__name) + ", "\
                 "address: " + str(self.__address) + ", "\
                 "tag: " + str(self.__tag) + ", "\
                 "latitude: " + str(self.__latitude) + ", "\
                 "longitude: " + str(self.__longitude)
        return str(string)

    # returns a GeoLocation object based on the input lat and long
    def get_location(self):
        location = GeoLocation(self.__latitude, self.__longitude)
        return location

    # returns the distance between this place and another
    def distance_from(self, spot):
        return self.get_location().distance_from(spot)
