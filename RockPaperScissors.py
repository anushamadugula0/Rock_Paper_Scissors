import random
user_choice=int(input("Enter your Choice: 0 for Rock✊, 1 for Paper✋ and 2 for Scissors✌️ :"))
if(user_choice==0):
    print("✊")
elif(user_choice==1):
    print("✋")
elif(user_choice==2):
    print("✌️")
if (user_choice>2 or user_choice<0):
    print("You entered a invalid choice You lose.")
else:
    computer_choice=random.randint(0,2)
    print("Computer Chose:")
    print(computer_choice)
    if(computer_choice==0):
        print("✊")
    elif(computer_choice==1):
        print("✋")
    elif(computer_choice==2):
        print("✌️")
    if(computer_choice==user_choice):
        print("It's a draw")
    elif(user_choice==0 and computer_choice==2):
        print("You win")
    elif(user_choice==2 and computer_choice==0):
        print("You loose")
    elif(user_choice>computer_choice):
        print("You win")
    elif(computer_choice>user_choice):
        print("You Loose")