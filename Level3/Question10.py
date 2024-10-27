def cafe_computer_simulation(N, visits):
    occupied_computers = 0
    turned_away_customers = 0

    for visit in visits:
        if visit == "arrive":
            if occupied_computers < N:
                occupied_computers += 1
            else:
                turned_away_customers += 1  
        elif visit == "leave":
            if occupied_computers > 0:
                occupied_computers -= 1

    return turned_away_customers

N = 2
visits = ["arrive", "arrive", "arrive", "leave", "arrive"]
output = cafe_computer_simulation(N, visits)
print(f"Customers turned away: {output}")
