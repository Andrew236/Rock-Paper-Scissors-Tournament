import random 
import time

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
correct_input = False
rounds = 0
playAgain = True

while playAgain:
    computer_choice = random.choice(choices)
    while correct_input == False:
        userchoice = input("rock, paper, or scissors?: ").lower()

        if userchoice not in choices:
            print("Please enter a valid pick.. try again")

        else:
            correct_input = True

    print("The computer has locked in their choice")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    rounds += 1

    if userchoice == "paper" and computer_choice == "paper":
        print("TIE")
        print(f"Computer choice: {computer_choice}")
        print(f"Your Choice: {userchoice}")

    if userchoice == "paper" and computer_choice == "rock":
        print("WINNER")
        print(f"Computer choice: {computer_choice}")
        print(f"Your Choice: {userchoice}")
        user_score +=1
    if userchoice == "paper" and computer_choice == "scissors":
        print("LOSER")
        print(f"Computer choice: {computer_choice}")
        print(f"Your Choice: {userchoice}")
        computer_score += 1

    if userchoice == "rock" and computer_choice == "rock":
        print("TIE")
        print(f"Computer choice: {computer_choice}")
        print(f"Your Choice: {userchoice}")

    if userchoice == "rock" and computer_choice == "scissors":
        print("WINNER")
        print(f"Computer choice: {computer_choice}")
        print(f"Your Choice: {userchoice}")
        user_score +=1
    if userchoice == "rock" and computer_choice == "paper":
        print("LOSER")
        print(f"Computer choice: {computer_choice}")
        print(f"Your Choice: {userchoice}")
        computer_score += 1
    if userchoice == "scissors" and computer_choice == "scissors":
        print("TIE")
        print(f"Computer choice: {computer_choice}")
        print(f"Your Choice: {userchoice}")

    if userchoice == "scissors" and computer_choice == "paper":
        print("WINNER")
        print(f"Computer choice: {computer_choice}")
        print(f"Your Choice: {userchoice}")
        user_score +=1
    if userchoice == "scissors" and computer_choice == "rock":
        print("LOSER")
        print(f"Computer choice: {computer_choice}")
        print(f"Your Choice: {userchoice}")
        computer_score += 1
    
    yes_or_no = input("Would you like to play another round? yes or no: ").lower()
    if user_score == computer_score:
        print("\n")
        print("The total score is tied! I suggest you try play another round")
        yes_or_no = input("Settle the tie? yes or no: ").lower()
    if yes_or_no == "yes":
        playAgain = True
        correct_input = False
        continue
    else:
        playAgain = False

    print(" ")
    print("TOTAL SCORE")
    print(f"USER: {user_score}")
    print(f"COMPUTER: {computer_score}")

    if computer_score > user_score:
        print(f"I am sorry the computer took this one after playing {rounds} rounds")
    elif computer_score < user_score:
        print(f"Congrats you won after playing {rounds} rounds")
    else:
        print("Looks like you guys tied after playing {rounds} rounds")
    