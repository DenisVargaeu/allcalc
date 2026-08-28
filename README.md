# ALLCALC 🧮

**ALLCALC** is a modular CLI calculator written in Python.

Instead of putting everything into one giant calculator, ALLCALC is built from separate mini-apps called **modules**. The main program acts as a launcher that lets you choose which module to run.

## Features

Currently available:

* ✅ Positive / Negative / Zero Checker
* ✅ Even / Odd Checker
* ✅ Grade Checker
* ✅ Basic Calculator CLI

### Basic Calculator

The Basic Calculator has its own interactive shell:

```text
BasicCalc> 10+20/12
Result: 11.666666666666666

BasicCalc> 5*8
Result: 40

BasicCalc> help
BasicCalc shell allows you to perform basic calculations.
```

It supports mathematical expressions using operators such as:

```text
+
-
*
/
%
**
()
```

Invalid expressions are handled with error messages instead of crashing the program.

## Project Structure

```text
ALLCALC/
├── app.py
├── modules/
│   ├── negativecheck.py
│   ├── evenodd.py
│   ├── grade.py
│   └── basiccalc.py
└── README.md
```

`app.py` is the main launcher and menu.

Each file inside `modules/` is designed as a separate mini-app that handles its own functionality.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/DenisVargaeu/allcalc.git
cd allcalc
```

### 2. Install the dependency

ALLCALC currently uses `simpleeval` for evaluating mathematical expressions.

```bash
pip install simpleeval
```

### 3. Run ALLCALC

```bash
python app.py
```

## Example

```text
Welcome to AllCalc
Please choose what you want to calculate:

1. Check if number is positive, negative or zero
2. Check if number is even or odd
3. Check your grade
Q. Exit

Please input your choice:
```
## Contributing

ALLCALC is a personal project, but suggestions, ideas and improvements are welcome.

## License

This project is currently unlicensed.
