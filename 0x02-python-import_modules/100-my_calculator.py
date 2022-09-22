#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    import calculator_1
    arg_check = len(argv[1:])
    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    result = 0
    if arg_check < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif operator == '+':
        result = calculator_1.add(a, b)
    elif operator == '-':
        result = calculator_1.sub(a, b)
    elif operator == '*':
        result = calculator_1.mul(a, b)
    elif operator == '/':
        result = calculator_1.add(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{a} {operator} {b} = {result}")
