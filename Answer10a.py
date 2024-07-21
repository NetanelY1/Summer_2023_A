class Room:
    def __init__(self, kind, area, freq):
        self.kind = kind
        self.area = area
        self.freq = freq

class App:
    def __init__(self, app_num, owner, rooms, rate):
        self.app_num = app_num
        self.owner = owner
        self.rooms = rooms
        self.rate = rate

class Building:
    def __init__(self, address, apartments):
        self.address = address
        self.apartments = apartments
