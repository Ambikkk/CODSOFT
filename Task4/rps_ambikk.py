#Task 4 - Rock Paper Scissors Game 
import random
USER = "Ambikk"
def generate_choices():
    base = ["rock", "paper", "scissors"]
    random.shuffle(base)
    return base

def get_user_choice(options):
    print("\nAvailable choices:", ", ".join(options))
    user = input("Enter your choice: ").strip().lower()
    if user not in options:
        print("Invalid choice, try again.")
        return get_user_choice(options)
    return user

def get_computer_choice(options):
    return random.choice(options)

def decide_winner(user, comp, options):
    ui = options.index(user)
    ci = options.index(comp)

    # winning logic based on circular index
    if ui == ci:
        return "tie"
    elif (ui - ci) % 3 == 1:
        return "user"
    else:
        return "computer"

def main():
    print("=== CODSOFT – TASK 4 Rock Paper Scissors (Ambikk) ===")

    options = generate_choices()

    user = get_user_choice(options)
    comp = get_computer_choice(options)

    result = decide_winner(user, comp, options)

    print(f"\nYou chose: {user}")
    print(f"Computer chose: {comp}")
    print(f"Result: {result.upper()} Won")

if __name__ == "__main__":
    main()
