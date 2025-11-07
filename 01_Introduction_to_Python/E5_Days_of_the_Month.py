# Define a dictionary where the keys are month numbers and the values are the number of days in those months.
month_days = {
    1: 31,   
    2: 28,   
    3: 31,   
    4: 30,   
    5: 31,   
    6: 30,   
    7: 31,   
    8: 31,   
    9: 30,   
    10: 31,  
    11: 30,  
    12: 31   
}

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# 2. Input Handling - Ask user for month number
month_number = int(input("Enter the month number (1-12): "))

# 3. Check and Output - Validate using an if-else statement and account for leap years
if month_number >= 1 and month_number <= 12:
    days = month_days[month_number]
    month_name = month_names[month_number]
    
    if month_number == 2:
        leap_year = input("Is it a leap year? (yes/no): ")
        if leap_year.lower() == "yes":
            days = 29
    
    print(f"{month_name} has {days} days.")
else:
    print("Invalid month number! Enter a valid month you dummy.")
