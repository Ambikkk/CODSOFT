# Task 2: Simple Calculator 
import time
from datetime import datetime

USER = "Ambikk"

def get_number(msg):
    for _ in range(3):
        value = input(msg).strip()
        try:
            return float(value)
        except ValueError:
            print("❌ Invalid number, try again.")
    raise SystemExit("Too many wrong attempts. Exiting.")

def get_operation():
    print("\nChoose an operation:")
    print("1) Addition (+)")
    print("2) Subtraction (-)")
    print("3) Multiplication (*)")
    print("4) Division (/)")
    print("5) Modulus (%)")
    print("6) Power (**)")

    return input("Enter choice (1–6): ").strip()

def log_history(a, op, b, result):
    with open("task2_history.txt", "a") as f:
        f.write(f"{datetime.now()} | {USER} | {a} {op} {b} = {result}\n")

def main():
    print("="*50)
    print("  CODSOFT – TASK 2: SIMPLE CALCULATOR".center(50))
    print(f"    Personalized for {USER}".center(50))
    print("="*50)

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    
    choice = get_operation()

    operations = {
        "1": ("+", lambda x, y: x + y),
        "2": ("-", lambda x, y: x - y),
        "3": ("*", lambda x, y: x * y),
        "4": ("/", lambda x, y: x / y if y != 0 else "Error: Division by zero"),
        "5": ("%", lambda x, y: x % y if y != 0 else "Error: Modulus by zero"),
        "6": ("**", lambda x, y: x ** y),
    }

    if choice not in operations:
        print("❌ Invalid choice.")
        return

    op_symbol, func = operations[choice]
    result = func(a, b)

    print(f"\nResult: {a} {op_symbol} {b} = {result}")
  
    if "Error" not in str(result):
        log_history(a, op_symbol, b, result)

if __name__ == "__main__":
    main()
