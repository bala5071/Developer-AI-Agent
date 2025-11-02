"""
Entry point for the simple calculator application.

Usage: Run this script and follow interactive prompts to perform calculations.

"""

from core.calculator import add, subtract, multiply, divide
from utils.validation import validate_number, InputValidationError


def main() -> None:
    """
    Runs the interactive calculator loop.

    Users can select operations, enter numbers, and get results.
    Handles validation and errors gracefully.

    Returns:
        None

    Examples:
        Run `python main.py` to start using the calculator.
    """
    print("Welcome to the Simple Calculator!")
    print("Supported operations: add, subtract, multiply, divide")
    print("Type 'clear' to reset, or 'exit' to quit.")

    current_value = 0.0
    while True:
        try:
            print(f"\nCurrent value: {current_value}")
            user_input = input("Enter an operation (add, subtract, multiply, divide) or command: ").strip().lower()

            if user_input == "exit":
                print("Goodbye!")
                break
            elif user_input == "clear":
                current_value = 0.0
                print("Calculator cleared.")
                continue
            elif user_input not in {"add", "subtract", "multiply", "divide"}:
                print("Invalid operation. Please enter a valid operation or command.")
                continue

            num_input = input("Enter the number to operate with: ").strip()
            number = validate_number(num_input)

            if user_input == "add":
                current_value = add(current_value, number)
            elif user_input == "subtract":
                current_value = subtract(current_value, number)
            elif user_input == "multiply":
                current_value = multiply(current_value, number)
            elif user_input == "divide":
                current_value = divide(current_value, number)

            print(f"Result: {current_value}")

        except InputValidationError as ive:
            print(f"Input error: {ive}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyboardInterrupt:
            print("\nExiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
