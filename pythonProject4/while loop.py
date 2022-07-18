while True:
    print("eneter + for addition")
    print("enter - for substraction")
    print("eneter * for multiplication")
    print("enter / for division")
    print("enter # for exit")

    sym = input("enter operator :-")

    if sym == "+":
        a = int(input("enter first number:-"))
        b = int(input("enter second number:-"))
        print("the addition of two number is", a + b)

    elif sym == "-":
        a = int(input("enter first number:-"))
        b = int(input("enter second number:-"))
        print("the substraction of two number is", a - b)

    elif sym == "*":
        a = int(input("enter first number:-"))
        b = int(input("enter second number:-"))
        print("the multiplication of two number is", a * b)

    elif sym == "/":
        a = int(input("enter first number:-"))
        b = int(input("enter second number:-"))
        print("the division of two number is", a / b)

    elif sym == "#":
        exit()
    else:
        print("invalid op