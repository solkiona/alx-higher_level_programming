#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    i = len(sys.argv) - 1

    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("{:d}".format(1))
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        sign = sys.argv[2]
        if sign == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            print("{:d}".format(0))
        elif sign == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            print("{:d}".format(0))
        elif sign == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            print("{:d}".format(0))
        elif sign == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
            print("{:d}".format(0))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            print("{:d}".format(1))
