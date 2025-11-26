# Task 3 - Password Generator
import secrets
import string

USER = "Ambikk"

def get_password_length():
    try:
        length = int(input("Enter password length: ").strip())
        return max(4, length)    
    except ValueError:
        print("Invalid input. Using length = 8")
        return 8

def get_complexity():
    print("\nChoose password complexity:")
    print("1) lowercase")
    print("2) lowercase + digits")
    print("3) letters + digits")
    print("4) letters + digits + symbols")

    choice = input("Enter choice (1–4): ").strip()

    if choice == "1":
        return string.ascii_lowercase
    elif choice == "2":
        return string.ascii_lowercase + string.digits
    elif choice == "3":
        return string.ascii_letters + string.digits
    elif choice == "4":
        return string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid input Defaulting to level 3")
        return string.ascii_letters + string.digits

def generate_password(chars, length):
    return "".join(secrets.choice(chars) for _ in range(length))

def main():
    print("=== CODSOFT – TASK 3 Password Generator (Ambikk) ===")

    length = get_password_length()
    chars = get_complexity()

    password = generate_password(chars, length)

    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
