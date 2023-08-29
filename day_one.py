print("Welcome to the Band Name Generator.")

run_again = True

def replay():
    play_again = input("Would you like to generate a new band name? ").lower()

    acceptable_answers = ["yes", "y" , "no", "n"]

    if play_again in acceptable_answers:
        if play_again == "yes" or play_again == "y":
            return True
        else:
            return False
    else:
        print("Please answer with a valid response (y, n, yes, or no)\n")
        replay()

while run_again:
    first_band_name = input("What's the name of the city you grew up in?: ")
    second_band_name = input("What pet would you like to have?: ")

    print(f"{first_band_name} {second_band_name}")

    run_again = replay()
