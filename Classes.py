# Classes defined to be used
class Package:
    """Define package class"""
    def __init__(self, id, address, city, state, zip, deadline, mass, notes, status, location_id):
        """initialize package object"""
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status
        self.location_id = location_id
        self.departure = None
        self.arrival = None
        self.truck = None

    def __str__(self):
        """reformat how package object is returned"""
        return '| {:^3} | {:^5} | {:^8} | {:^8} | {:^24} | {:^8} |'\
            .format(self.id, self.truck, self.departure.strftime('%H:%M'), self.arrival.strftime('%H:%M'),
                    self.status, self.deadline.strftime('%H:%M'))


class Location:
    """Define location class"""
    def __init__(self, id, name, address, city, state, zip):
        """initialize location object"""
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        """reformat how location object is returned"""
        return "%3s %45s %40s" % (self.id, self.name, self.address)


class Format:
    """Define Format class for string formatting"""
    BLUE = '\33[94m'
    YELLOW = '\33[93m'
    GREEN = '\33[92m'
    RED = '\33[91m'
    BOLD = '\33[01m'
    UNDERLINE = '\33[04m'
    END = '\33[0m'


class Status:
    """Define Status class"""
    AT_HUB = Format.BLUE + 'AT_HUB' + Format.END
    EN_ROUTE = Format.YELLOW + 'EN_ROUTE' + Format.END
    DELIVERED = Format.GREEN + 'DELIVERED' + Format.END
    LATE = Format.RED + 'LATE' + Format.END
