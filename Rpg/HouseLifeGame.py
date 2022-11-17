import time
import random


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        for option in options:
            if option in response:
                return option
        print_pause("Sorry, I don't understand.")


def garden(items, times):
    valid_garden_inputs = ["1", "2", "3", "4"]
    if times == 0:
        print(
            "\n\nYou unlock the door and get out\n"
            "in the garden. The air is cool. You\n"
            "have many different plants that need\n"
            "taken care of.\n\n")
        times = 1
    else:
        print("\n\nYou are in the garden\n")
        response = valid_input(
            "What do you want to do?\n"
            "1. Water the flowers\n"
            "2. Pick up crops\n"
            "3. Transfer lillies in a bigger pot\n"
            "4. Go inside\n", valid_garden_inputs)
        if response == "1":
            if "watered" in items:
                print("You already did that")
            else:
                items.append("watered")
                print("You water the flowers\n")
        elif response == "2":
            if "basket" in items:
                print(
                    "\n\nYou harvest tomatoes, cherries,\n"
                    "pears, blackcurrants, and corn.\n"
                    "You take the basket in the kitchen\n\n")
                items.append("full_basket")
                kitchen(items, 1)
            else:
                print(
                    "\n\nYou need a basket. You recall\n"
                    "seeing your basket inside the shelf\n"
                    "under the sink\n\n")
        elif response == "3":
            if "bouquet" in items:
                print("\n\nYou already did that\n\n")
            else:
                print(
                    "\n\nYou transfer the lillies to a bigger pot\n"
                    "You also make a bouquet for your wife\n\n")
                items.append("bouquet")
        else:
            print("\n\nYou go in the living room\n\n")
            living_room(items, 1)
    garden(items, times)


def kitchen(items, times):
    valid_kitchen_inputs = ["1", "2", "3", "4"]
    if times == 0:
        times = 1
        print(
            "\n\nYou are standing in the kitchen\n"
            "in front of the sink. On your left\n"
            "your left you have a kettle, and on\n"
            "your right the stove\n")
    elif times == 1:
        print(
            "\n\nYou are standing in the kitchen\n"
            "in front of the sink\n")
    if "basket" not in items:
        response = valid_input(
            "What do you want to do?\n"
            "1. Make tea\n"
            "2. Cook breakfast\n"
            "3. Get the basket\n"
            "   that is in the\n"
            "   shelf under the\n"
            "   sink\n"
            "4. Go to the living room\n", valid_kitchen_inputs)
    else:
        if "basket" in items:
            if "full_basket" not in items or "empty_basket" in items:
                response = valid_input(
                    "What do you want to do?\n"
                    "1. Make tea\n"
                    "2. Cook breakfast\n"
                    "3. Drink some water\n"
                    "4. Go to the living room\n", valid_kitchen_inputs)
        if "full_basket" in items and "empty_basket" not in items:
            response = valid_input(
                "What do you want to do?\n"
                "1. Make tea\n"
                "2. Cook breakfast\n"
                "3. Taxinomise harvest in the fridge\n"
                "4. Go to the living room\n", valid_kitchen_inputs)
    if response == "1":
        if "cup" in items:
            print(
                "\n\nYou already had a cup of tea\n"
                "Drinking more could upset your\n"
                "stomach.\n\n")
        else:
            items.append("cup")
            print(
                "\n\nYou pick up your cup. You boil\n"
                "some water in the kettle and then\n"
                "prepare some jasmine tea. You enjoy \n"
                "it with a piece of chocolate.\n\n")
    elif response == "2":
        if "pan" not in items:
            items.append("pan")
            print(
                "\n\nYou use your new copper pan\n"
                "to cook breakfast. You slow\n"
                "fry in olive olive five tomatoes\n"
                "cut in half. You also add one whole\n"
                "garlic finely chopped, as well as \n"
                "black pepper, and salt. In the end\n"
                "you add four eggs on top of that mix\n"
                "and you allow them to get cooked but \n"
                "not too much. You enjoy your breakfast.\n\n")
        else:
            print(
                "\n\nYou already had breakfast.\n"
                "Eating again would not be the\n"
                "healthiest choice\n")
            if ("cup" in items and "bouquet" in items and
                    "full_basket" in items and "empty_basket" in items):
                print("\nYou should consider taking some rest\n\n")
            elif ("cup" in items and
                  ("bouquet" not in items or
                   "full_basket" not in items or
                   "empty_basket" not in items)):
                print(
                    "You could do some activity\n"
                    "I believe that there might be some \n"
                    "unfinished activities left in\n"
                    "the garden.\n\n")
            elif "cup" not in items:
                print(
                    "You could have a cup of tea with\n"
                    "some chocolate for dessert\n\n")
    elif response == "3":
        if "basket" not in items:
            items.append("basket")
            print("\n\nYou pick up the basket")
        elif "basket" in items and "full_basket" not in items:
            print("\n\nYou drink some water\n\n")
        elif "empty_basket" not in items and "full_basket" in items:
            print(
                "\n\nYou taxinomize your harvest in\n"
                "the appropriate fridge shells\n\n")
            items.append("empty_basket")
        elif "empty_basket" in items:
            print("\n\nYou drink some water.\n\n")
            if ("paper" in items and
                    "cup" in items and
                    "pan" in items and
                    "watered" in items and
                    "bouquet" in items and
                    "vase" in items):
                device_choices = ["laptop", "XBox", "PS4", "iPhone"]
                device = random.choice(device_choices)
                print(
                    "\n\nYou are really tired."
                    "\nYou sit on your couch and\n"
                    "\nplay a video game in your " + device + "."
                                                              "\nThank you for playing!!\n\n")
                accepted_inputs = ["yes", "no"]
                response = valid_input(
                    "\nWould you like to play again? Yes/No: ",
                    accepted_inputs)
                if response == "no":
                    print("\nThank you for playing. Bye now!!!")
                    exit()
                else:
                    play_game()
        else:
            if "basket" in items:
                print(
                    "\n\nYou have already picked up basket\n"
                    "out of the shelf\n\n")
    else:
        living_room(items, 1)
    kitchen(items, 1)


def living_room(items, times):
    accepted_living_room_inputs = ["1", "2", "3"]
    accepted_living_room_inputs_2 = ["1", "2", "3", "4"]

    if times == 1:
        print("\n\nYou are standing in the living room\n"
              "in front of the door to the garden\n")
    if "bouquet" not in items:
        response = valid_input("What do you want to do?\n"
                               "1. Go out\n"
                               "2. Sit down\n"
                               "3. Go to the kitchen\n",
                               accepted_living_room_inputs)
    elif "vase" in items:
        response = valid_input("What do you want to do?\n"
                               "1. Go out\n"
                               "2. Sit down\n"
                               "3. Go to the kitchen\n"
                               "4. Smell the lillies\n",
                               accepted_living_room_inputs_2)
    else:
        response = valid_input("What do you want to do?\n"
                               "1. Go out\n"
                               "2. Sit down\n"
                               "3. Go to the kitchen\n"
                               "4. Put lillies bouquet on the vase\n",
                               accepted_living_room_inputs_2)
    if response == "1":
        if "keys" in items:
            garden(items, 0)
        else:
            print("\n\nYou dont have keys and the door is locked\n\n")
            living_room(items, 0)
    elif response == "2":
        desk(items)
    elif response == "3":
        kitchen(items, 0)
    else:
        if "vase" in items:
            print("\n\nYou smell the lillies\n\n")
            living_room(items, 1)
        else:
            print("\nYou put the lillies in a vase\n")
            items.append("vase")
            living_room(items, times)


def desk(items):
    valid_desk_inputs = ["1", "2", "3"]
    if "in_desk" not in items:
        print("\n\nYou sit down on your desk,\n"
              "that is next to the window.\n")
    if "paper" not in items and "keys" not in items:
        print("In a little box on your right you\n"
              "see the keys for the garden door.\n"
              "as well as some pencils and papers\n\n")
    elif "paper" in items and "keys" not in items:
        print("In front of you, you see the paper\n"
              "with the drawings you did earlier.\n"
              "On the little box on your right there"
              "is the key for the garden door\n\n")
    elif "paper" not in items and "keys" in items:
        print("You look at the paper and pencils\n"
              "that are there\n\n")
    else:
        print("You look at your drawing\n\n")
    if "keys" not in items:
        response = valid_input("What do you want to do?\n"
                               "1. Pick keys up\n"
                               "2. Draw a picture\n"
                               "3. Stand up\n", valid_desk_inputs)
        if response == "1":
            print("\n\nYou pick up the keys and put\n"
                  "them in your pocket\n\n")
            items.append("keys")
        elif response == "2":
            print("\n\nYou do some drawing\n")
            drawing_choices = ["dinosaur", "cupcake", "bird"]
            drawing = random.choice(drawing_choices)
            print("You drew a " + drawing + "\n\n")
            items.append("paper")
        elif response == "3":
            if "in_desk" in items:
                items.remove("in_desk")
            living_room(items, 1)
        if "in_desk" not in items:
            items.append("in_desk")
        desk(items)
    else:
        response = valid_input("\n\n1. Draw a picture\n\n"
                               "2. Stand up\n", ["1", "2"])
        if response == "1" and "paper" in items:
            print("\n\nYou have no more paper left\n\n")
            if "in_desk" not in items:
                items.append("in_desk")
            desk(items)
        elif response == "1" and "paper" not in items:
            print("\n\nYou do some drawing\n\n")
            items.append("paper")
            if "in_desk" not in items:
                items.append("in_desk")
            desk(items)
        else:
            if "in_desk" in items:
                items.remove("in_desk")
            living_room(items, 1)


def instructions(times):
    if times == 0:
        times = 1
        print_pause("Welcome to House Life!\n\n"
                    "Developed by Dimitrios Malonas\n")
    print_pause("\nTo play the game you make choices\n"
                "based on the different menu options.\n"
                "You need to find the correct sequence\n"
                "of activities to finish the game\n"
                "(One example sequence is: [no, 2, 2, 1,"
                "2, 3, 1, 1, 2, 2, 3, 3, 4, 1,"
                "1, 3, 4, 4, 1, 2, 3, 3]")
    response = valid_input("Do you need more instructions?\n1. Yes\n2. No\n", ["yes", "no"])

    if response == "yes":
        instructions(times)


def intro(items):
    print_pause("\n\nYou are going to spend a Saturday morning"
                "\nrelaxing at home. It is a sunny day."
                "\nYou are standing in the living room in"
                "\nfront of the door that leads to the garden\n")
    living_room(items, 0)


def print_pause(string_input):
    time.sleep(2)
    print(string_input)
    print("\n")


def play_game():
    times = 0
    items = []
    instructions(times)
    intro(items)


if __name__ == '__main__':
    play_game()

# play_game()
