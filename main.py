#Lunch Till Program
import json

lunch_items_saved = {
    "pasta": 1.50,
    "pasta+sauce": 1.75,
    "puddings": 1.20,
    "vegetable_pot": 1.00,
    "yoghurt_pot": 0.50,
    "fruit": 0.75,
    "cookies": 1.00,
    "meat": 999.99,
    "beans": 0.50,
    "juice_large": 1.00,
    "juice_medium": 0.50,
    "juice_small": 0.25,
    "water": 1.50,
    "milk": 0.75
}

people = {
    "UserOne": 20.65,
    "UserTwo": 12.20,
}

with open('lunch_items_saved.txt', 'w') as json_file:
    json.dump(lunch_items_saved, json_file)

#with open('lunch_items_saved.txt') as file:
#    lunches = json.load(file)

def options(total_previous):

    #Add Previous Costs
    total = 0 + total_previous

    #Asks For Food Choice
    option = input("What is your food choice? ")

    #Prints price based on dictionary definition
    print(option, ": £", lunch_items_saved[option])

    #Adds item to total costs
    total += lunch_items_saved[option]

    #Asks if they 
    repeat = input("Anything else (Y/N): ")
    if repeat == "Y":
        options(total)
    elif repeat == "N":
        print("Your total cost is £", total)
    else:
        print("NULL")
        options(total)

options(0)

