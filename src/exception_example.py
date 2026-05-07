def available_seats(capacity, reserved):
    return capacity - reserved

def price_per_available_seat(total_ticket_revenue, capacity, reserved):
    seats_left = available_seats(capacity, reserved)
    return total_ticket_revenue / seats_left

def print_trip_report(trips):
    for trip in trips:
        train = trip["train"]
        revenue = trip["revenue"]
        capacity = trip["capacity"]
        reserved = trip["reserved"]
        price = price_per_available_seat(revenue, capacity, reserved)
        print(f"{train}: €{price:.2f} revenue per available seat")

def main():
    trips = [
        {"train": "IC 3021", "revenue": 4800, "capacity": 240, "reserved": 180},
        {"train": "IC 1745", "revenue": 3100, "capacity": 180, "reserved": 155},
        {"train": "SPR 812", "revenue": 2200, "capacity": 160, "reserved": 160},
        {"train": "IC 9090", "revenue": 5200, "capacity": 260, "reserved": 210},
    ]
    print_trip_report(trips)

main()
