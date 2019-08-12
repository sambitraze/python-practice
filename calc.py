
def calc():
    running = True
    a = int(input("Enter a nummber:"))
    while True:
        opr = input("Enter operator:")
        if(opr == '='):
            break
        b = int(input("ENter another number:"))
        if opr == "+":
            a = a + b
        elif opr == "-":
            a = a - b
        elif opr == "*":
            a = a * b
        elif opr == "/":
            a = a / b
        else :
            print("Invalid operator")
            break
    print("Result: ", a)

calc()