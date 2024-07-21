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

    def month_cost(self):
        total_cost = 0
        for room in self.rooms:
            total_cost += room.area * room.freq * self.rate
        return total_cost

class Building:
    def __init__(self, address, apartments):
        self.address = address
        self.apartments = apartments

def month_report(builds, clients):
    for client in clients:
        total_payment = 0
        print(f"Client: {client}")
        for building in builds:
            for app in building.apartments:
                if app.owner == client:
                    monthly_cost = app.month_cost()
                    total_payment += monthly_cost
                    print(f"  Apartment number: {app.app_num}")
                    print(f"  Address: {building.address}")
                    print(f"  Monthly cleaning cost: {monthly_cost}")
        print(f"Total monthly payment for {client}: {total_payment}\n")



# יצירת חדרים
room1 = Room("Bedroom", 20, 2)
room2 = Room("Bathroom", 10, 4)
room3 = Room("Kitchen", 15, 3)
room4 = Room("Living Room", 25, 2)
room5 = Room("Office", 10, 1)
room6 = Room("Bedroom", 30, 1)
room7 = Room("Bathroom", 12, 2)
room8 = Room("Kitchen", 18, 3)

# יצירת דירות
app1 = App(101, "John Doe", [room1, room2, room3], 5)
app2 = App(102, "Jane Smith", [room4, room5], 6)
app3 = App(103, "John Doe", [room6, room7], 5)
app4 = App(201, "Alice Johnson", [room8], 7)
app5 = App(202, "Bob Brown", [room1, room3, room5], 4)
app6 = App(203, "Alice Johnson", [room2, room4, room6], 6)

# יצירת בניינים
building1 = Building("123 Main St", [app1, app2, app3])
building2 = Building("456 Elm St", [app4, app5])
building3 = Building("789 Oak St", [app6])

# הפעלת דוח חודשי
month_report([building1, building2, building3], ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown"])
