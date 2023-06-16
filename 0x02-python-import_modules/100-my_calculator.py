#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    i = len(sys.argv) - 1

    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        sign = sys.argv[2]

        if sign != '+' and sign != '-' and sign != '*' and sign != '/':
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

        if sign == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
            sys.exit(0)
        elif sign == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
            sys.exit(0)
        elif sign == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
            sys.exit(0)
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
            sys.exit(0)
