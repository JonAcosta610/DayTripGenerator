destinations = ["Jamaica", "Hawaii", "Aruba", "Mal Dives", "Dominican Republic", "Puerto Rico"]
restaurants = ["Cara Mia", "Applebees", "Reethi Restaurant", "Symphony Restaurant", "Sea House Cafe", "Murphys West End Restaurant"]
mode_of_transportation = ["plane", "cruise ship", "train", "car", "bus", "motorcycle", "mopeds", "bicycles"]
entertainment_list = ["bus tour", "scuba diving", "dolphin watching", "surfing", "plantation tours", "historic site tours"]

import random

random_destination = random.choice(destinations)
random_restaurant = random.choice(restaurants)
random_transportation = random.choice(mode_of_transportation)
random_entertainment = random.choice(entertainment_list)

print("Welcome to Trip Planner! Where we will plan your trip.")

def day_trip_generator():
    print(f"Destination: {random_destination}")
    print(f"Restaurant: {random_restaurant}")
    print(f"Mode of Transportation: {random_transportation}")
    print(f"Entertainment: {random_entertainment}")
day_trip_generator()

def itinerary():
    user_satisfaction = input("Are you satisfied with this trip? Yes or No ")
    while user_satisfaction == "No":
        user_replace = input("What selection do you want to replace? ")
        if user_replace == "Destination":
            random_destination = random.choice(destinations)
            day_trip_generator()

        elif user_replace == "Restaurant":
            random_restaurant = random.choice(restaurants)
            day_trip_generator()

        elif user_replace == "Mode of Transportation":
            random_transportation = random.choice(mode_of_transportation)
            day_trip_generator()

        elif user_replace == "Entertainment":
            random_entertainment = random.choice(entertainment_list)
            day_trip_generator()
    
    user_satisfaction = input("Are you satisfied with this trip? Yes or No ")
itinerary()