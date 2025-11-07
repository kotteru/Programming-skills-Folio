# Have the user input their name, hometown, and age instead of hardcoding the values. 
# Store the information (name, hometown, and age) as key-value pairs in a dictionary.
# Print the values on separate lines using a single pirnt() statement

print("Please enter your information:")
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")

while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        if age > 0:
            break
        else:
            print("Please enter a positive number for age.")
    except ValueError:
        print("Invalid input! Please enter a numeric value for age.")

person = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(f"\n--- Your Profile ---\nName: {person['name']}\nHometown: {person['hometown']}\nAge: {person['age']}")
