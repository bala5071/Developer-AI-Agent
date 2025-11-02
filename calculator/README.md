# Simple Calculator 

A simple, interactive calculator tool implemented in Python to perform basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division

Built for anyone needing a straightforward calculator with error handling and clear usage.

---

## Key Features 

- ➕ Addition, ➖ Subtraction, ✖️ Multiplication, ➗ Division
- 🛑 Handles division by zero and invalid inputs gracefully
- 🧪 Fully unit tested and validated
- 📚 Well-documented code and clear module structure
- 🔧 Easy to install and run with minimal dependencies

---

## Technology Stack

- Python 3.9.7
- Pytest 6.2.5 (for testing)
- Flake8 4.0.1 (for linting)
- Black 21.12a1 (for code formatting)

---

## System Requirements

- Python 3.9.7 or higher
- Supported on Windows, macOS, Linux

---

## Installation

1. Clone the repository:

```
git clone <repository-url>
cd calculator
```

2. Create a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## Configuration

- Edit `.env` file or set environment variables directly
- Key variable:
  - `DEBUG`: `True` for detailed logging, `False` for production

---

## Usage

Run the calculator interactive script:

```
python src/main.py
```

Follow the on-screen prompts to enter operations and numbers. Commands:
- `add`, `subtract`, `multiply`, `divide` - arithmetic operations
- `clear` - reset current calculation
- `exit` - quit the calculator

Example session:
```
Welcome to the Simple Calculator!
Supported operations: add, subtract, multiply, divide
Type 'clear' to reset, or 'exit' to quit.

Current value: 0.0
Enter an operation (add, subtract, multiply, divide) or command: add
Enter the number to operate with: 5
Result: 5.0

Current value: 5.0
Enter an operation (add, subtract, multiply, divide) or command: multiply
Enter the number to operate with: 3
Result: 15.0
```

---

## Testing

Run unit tests using pytest:

```
pytest
```

---

## Development

- Code formatted with Black
- Lint code with Flake8

---

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

---

## License

MIT License

---

## Credits

Developed by the OpenAI Senior Full-Stack Software Engineer.

---

## Troubleshooting

- Ensure Python 3.9.7 is installed
- Activate the virtual environment before running or installing dependencies
- For input errors, enter valid numeric values

---

## Future Enhancements

- Extend to scientific calculator features
- Add GUI or web interface
- Support expression evaluation

---

(Include screenshots or GIFs demonstrating usage and output in `docs/usage` directory if desired.)
