print("Welcome to the tip calculator")

total = float(input("What was the total bill? $"))
perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

cal = round((total / split) * (1 + perc / 100), 2)

print(f"Each person should pay: ${cal}")