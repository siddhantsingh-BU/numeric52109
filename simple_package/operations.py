###
## simple_package - Module operations.py
## Basic online calculator
###
## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface function
##    that will prompt the user for input and
##    call the appropriate function based on the
##    user's input. The interface function should
##    continue to prompt the user for input until
##    the user enters'exit'. 
##
## 2) The interface function should also handle
##    any exceptions that might be thrown by the
##    basic operations functions. If an exception 
##    is thrown,the interface function should print 
##    an error message and continue to prompt the 
##    user for input.
##
## 3) Add other "operations" to the calculator, that
##    involve complicated operations (e.g., 
##    trigonometric functions, logarithms, etc.).
##

import math

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b


def _format_number(x):
    if isinstance(x, float) and x.is_integer():
        return int(x)
    return x


def calculator_interface():
    """Simple command-line interface for the calculator.

    Commands:
      - add x y
      - subtract x y
      - multiply x y
      - divide x y
      - sin x, cos x, tan x
      - log x (natural), log10 x
      - sqrt x
      - pow x y
      - help, exit

    The interface will catch and print errors, and continue looping until
    the user types 'exit'.
    """
    ops = {
        'add': (add, 2),
        'subtract': (subtract, 2),
        'sub': (subtract, 2),
        'multiply': (multiply, 2),
        'mul': (multiply, 2),
        'divide': (divide, 2),
        'div': (divide, 2),
        'sin': (math.sin, 1),
        'cos': (math.cos, 1),
        'tan': (math.tan, 1),
        'log': (math.log, 1),
        'log10': (math.log10, 1),
        'sqrt': (math.sqrt, 1),
        'pow': (math.pow, 2),
    }

    help_text = ("Enter a command and numbers, e.g. 'add 2 3' or 'sin 0.5'. "
                 "Type 'help' to see this message again, or 'exit' to quit.")

    print("Simple calculator. Type 'help' for instructions, 'exit' to quit.")
    while True:
        try:
            line = input('calc> ').strip()
        except (EOFError, KeyboardInterrupt):
            print('\nExiting.')
            break

        if not line:
            continue
        if line.lower() == 'exit':
            break
        if line.lower() == 'help':
            print(help_text)
            continue

        parts = line.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd not in ops:
            print(f"Unknown command: {cmd}. Type 'help' for usage.")
            continue

        func, arity = ops[cmd]
        if len(args) != arity:
            print(f"{cmd} expects {arity} argument(s); got {len(args)}")
            continue

        try:
            nums = [float(a) for a in args]
            result = func(*nums)
            print(_format_number(result))
        except ValueError:
            print("Error: could not parse number(s).")
        except ZeroDivisionError:
            print("Error: division by zero.")
        except OverflowError:
            print("Error: numerical result out of range.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    calculator_interface()
