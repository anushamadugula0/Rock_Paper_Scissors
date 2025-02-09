import random
score=0
game_over=False
while not game_over:
    user_choice=input("Enter your Choice: 0 for Rock✊, 1 for Paper✋ and 2 for Scissors✌️ and press 'x' for exit:")
    if user_choice=='x':
        print(f"your final score is {score}")
        game_over=True
    elif user_choice.isdigit():
        user_choice=int(user_choice)
    if(user_choice==0):
        print("✊")
    elif(user_choice==1):
        print("✋")
    elif(user_choice==2):
        print("✌️")
    if user_choice=='x':
        print(f"your final score is {score}")
        game_over=True
    elif user_choice.isdigit():
        user_choice=int(user_choice)
    elif user_choice!=0 and user_choice!=1 and user_choice!=2 and user_choice!='x':
        print("You have entered an invalid choice play again!!")
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
            print(f"score={score}")
            print("It's a draw")
        elif(user_choice==0 and computer_choice==2):
            score+=1
            print(f"your score={score}")
            print("You win")
        elif(user_choice==2 and computer_choice==0):
            print(f"your score={score}")
            print("You loose")
        elif(user_choice>computer_choice):
            score+=1
            print(f"your score={score}")
            print("You win")
        elif(computer_choice>user_choice):
            print(f"your score={score}")
            print("You Loose")
