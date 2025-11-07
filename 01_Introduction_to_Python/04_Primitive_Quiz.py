# Ask the user a Quiz
answer = input("What is the capital of France? ")

# requirement: (ignore case sensitivity)
paris_ics = ['paris', 'pariS', 'parIs', 'parIS', 'paRis', 'paRiS', 'paRIs', 'paRIS', 'pAris', 'pAriS', 'pArIs', 'pArIS', 'pARis', 'pARiS', 'pARIs', 'pARIS', 'Paris', 'PariS', 'ParIs', 'ParIS', 'PaRis', 'PaRiS', 'PaRIs', 'PaRIS', 'PAris', 'PAriS', 'PArIs', 'PArIS', 'PARis', 'PARiS', 'PARIs', 'PARIS']

if answer == paris_ics:
    print("Correct! The answer is Paris.")
else:
    print("Wrong! The correct answer is Paris.")


print("-----Biography Quiz ! (Multiple Choice 10 items) -----")

quiz_data = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Greece": "Athens",
    "Poland": "Warsaw",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Vienna"
}

print("Biography Quiz! (answers must be case sensitive)\n")

# For Loop through each question
for country, correct_answer in quiz_data.items():
    user_answer = input(f"What is the capital of {country}? ")
    if user_answer == correct_answer:
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is {correct_answer}.\n")

print("END")
