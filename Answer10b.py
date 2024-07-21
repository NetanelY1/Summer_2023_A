class App:
    def __init__(self, app_num, owner, rooms, rate):
        self.app_num = app_num
        self.owner = owner
        self.rooms = rooms
        self.rate = rate

    def month_cost(self):
        total_cost = 0
        for room in self.rooms:
            total_cost += room.area * room.freq * self.rate
        return total_cost
