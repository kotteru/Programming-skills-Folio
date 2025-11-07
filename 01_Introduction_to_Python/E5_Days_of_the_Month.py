# Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
month_days = {
    1: 31,   # January
    2: 28,   # February
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Input Handling: Ask the user for a month number
month_number = int(input("Enter the month number (1-12): "))

# 3. Check and Output: Use an if-else statement to Validate
if month_number >= 1 and month_number <= 12:
    print(f"Month {month_number} has {month_days[month_number]} days.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")
