# Classes defined to be used
class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, notes, status, location_id):
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

    def __str__(self):
        return "%3s %10s %10s" % (self.id, self.deadline, self.status)


class Location:
    def __init__(self, id, name, address, city, state, zip):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return "%3s %45s %40s" % (self.id, self.name, self.address)


class Format:
    BLUE = '\33[94m'
    YELLOW = '\33[93m'
    GREEN = '\33[92m'
    RED = '\33[91m'
    BOLD = '\33[01m'
    UNDERLINE = '\33[04m'
    END = '\33[0m'


class Status:
    AT_HUB = Format.BLUE + 'AT_HUB' + Format.END
    EN_ROUTE = Format.YELLOW + 'EN_ROUTE' + Format.END
    DELIVERED = Format.GREEN + 'DELIVERED' + Format.END
    LATE = Format.RED + 'LATE' + Format.END
