print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15: "))
people = int(input("How many people are splitting the bill? "))
pay = (total * (1 + tip / 100)) / people
print(f"Each person should pay: ${pay:.2f}")