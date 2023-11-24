import random

while True:
    user_choice = input("Enter a choice (Rock,Paper,Scissors)")
    possible_choice = ["Rock","Paper","Scissors"]
    computer_choice = random.choice(possible_choice)
    print(f"\nYou choose{user_choice},computer chose{computer_choice}")
    
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}.It's a tie!")
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print(f"Rock smashes scissors.You win!")
        else:
            print(f"Paper covers rock.Computer wins.")
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print(f"Scissors cuts paper.You win!")
        else:
            print(f"Rock crushes scissors.Computer wins.")
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print(f"Paper covers rock.You win!")
        else:
            print(f"Scissors cuts paper.Computer wins.")
    play_again = input("Play again?(y/n): ")
    if play_again.lower() != "y":
        break