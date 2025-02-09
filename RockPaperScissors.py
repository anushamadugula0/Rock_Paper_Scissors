import random

score = 0
game_over = False

while not game_over:
    user_choice = input("Enter your Choice: 0 for Rock✊, 1 for Paper✋ and 2 for Scissors✌️ and press 'x' for exit: ")

    if user_choice.lower() == 'x':
        print(f"Your final score is {score}")
        break  # Exit the loop

    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice not in [0, 1, 2]:  # Validate input
            print("Invalid choice! Please enter 0, 1, or 2.")
            continue
    else:
        print("Invalid input! Please enter a number (0, 1, 2) or 'x' to exit.")
        continue

    choices = ["✊", "✋", "✌️"]
    print(f"You chose: {choices[user_choice]}")

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {choices[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        score += 1
        print(f"You win! Your score: {score}")
    else:
        print(f"You lose! Your score: {score}")

