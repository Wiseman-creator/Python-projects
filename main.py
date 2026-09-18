import random

print("Welcome to Snake - Water - Gun!")
print("Choices: Snake, Water, Gun")

choices = ["Snake", "Water", "Gun"]

user_choice = input("Enter your choice (Snake/Water/Gun): ").strip().title()

computer_choice = random.choice(choices)

if user_choice not in choices:
    print("Invalid input! Please enter Snake, Water, or Gun.")
else:
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a Draw!")
    elif (
        (user_choice == "Snake" and computer_choice == "Water")
        or (user_choice == "Water" and computer_choice == "Gun")
        or (user_choice == "Gun" and computer_choice == "Snake")
    ):
        print("Result: You Win!")
    else:
        print("Result: You Lose!")

