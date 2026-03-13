from nlp_parser import parse_query
from flight_search import search_flights

user_input = input("Where do you want to travel? ")

origin, destination, date = parse_query(user_input)

flights = search_flights(origin, destination, date)

print("\nFlights found:\n")

for flight in flights:
    print(flight["airline"], flight["time"])
