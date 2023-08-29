print("Welcome to the tip calculator.")

initial_total = float(input("What was the total bill?: "))
amount_of_splits = float(input("\nHow many people to split the bill?: "))
split_percentage = float(
    input("\nWhat percentage tip would you like to give? 10, 12 or 15?: ")) / 100

total = initial_total / amount_of_splits
tip = (initial_total / amount_of_splits) * split_percentage
final_total = round(total + tip, 2)

print(f"\nEach person should pay {final_total}.")
