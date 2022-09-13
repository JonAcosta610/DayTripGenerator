destinations = ["Jamaica", "Hawaii", "Aruba", "Mal Dives", "Dominican Republic", "Puerto Rico"]
restaurants = ["Cara Mia", "Applebees", "Reethi Restaurant", "Symphony Restaurant", "Sea House Cafe", "Murphys West End Restaurant"]
mode_of_transportation = ["plane", "cruise ship", "train", "car", "bus", "motorcycle", "mopeds", "bicycles"]
entertainment_list = ["bus tour", "scuba diving lesson", "dolphin watching tour", "surfing lesson", "plantation tour", "historic site tour"]

import random

def welcome():
    print("Welcome to Trip Planner! \nWhere we will plan your trip.\n")

# def randomizer(random_destination, random_restaurant, random_transportation, random_entertainment):
random_destination = random.choice(destinations)
random_restaurant = random.choice(restaurants)
random_transportation = random.choice(mode_of_transportation)
random_entertainment = random.choice(entertainment_list)
 
def trip_randomizer(random_destination, random_restaurant, random_transportation, random_entertainment):
    print(f"Destination: {random_destination}")
    print(f"Restaurant: {random_restaurant}")
    print(f"Mode of Transportation: {random_transportation}")
    print(f"Entertainment: {random_entertainment}")

def itinerary(random_destination, random_restaurant, random_transportation, random_entertainment):
    user_satisfaction = input("Are you satisfied with this trip? Yes or No ")
    while user_satisfaction == "No" or user_satisfaction == "NO" or user_satisfaction == "no":
        user_replace = input("\nWhat selection do you want to replace? ")
        if user_replace == "1":
            random_destination = random.choice(destinations)
            print(random_destination)
            
        elif user_replace == "2":
            random_restaurant = random.choice(restaurants)
            print(random_restaurant)
            
        elif user_replace == "3":
            random_transportation = random.choice(mode_of_transportation)
            print(random_transportation)
            
        elif user_replace == "4":
            random_entertainment = random.choice(entertainment_list)
            print(random_entertainment)
               
        user_satisfaction = input("Are you satisfied with this trip? Yes or No ")

    else:
        print("\nFantastic! \nHave a safe trip! \nYour itineray is below.\n")
        print(f"Destination: {random_destination}")
        print(f"Restaurant: {random_restaurant}")
        print(f"Mode of Transportation: {random_transportation}")
        print(f"Entertainment: {random_entertainment}")    

def master_function():
    welcome()
    # randomizer(random_destination, random_restaurant, random_transportation, random_entertainment)
    trip_randomizer(random_destination, random_restaurant, random_transportation, random_entertainment)
    itinerary(random_destination, random_restaurant, random_transportation, random_entertainment)
master_function()