import random

choices = ["rock", "paper", "scissors"]

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissor.")
        user_choice = input("Enter your choice (rock/paper/scissor): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou choose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_again():
    return input("\nDo you want to play again? (yes/no): ").lower() == "yes"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        display_result(user_choice, computer_choice, winner)
        print(f"\nScore -> You: {user_score} | Computer: {computer_score}")

        if not play_again():
            break
    
    print("\nThank you for playing! Final Score -> You: {user_score} | Computer: {computer_score}")

if __name__ == "__main__":
    main()
