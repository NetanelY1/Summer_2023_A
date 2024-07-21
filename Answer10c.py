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
