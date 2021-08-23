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


class Status:
    AT_HUB = '\33[94m' + 'AT_HUB' + '\33[0m'
    EN_ROUTE = '\33[93m' + 'EN_ROUTE' + '\33[0m'
    DELIVERED = '\33[92m' + 'DELIVERED' + '\33[0m'
    LATE = '\33[91m' + 'LATE' + '\33[0m'
