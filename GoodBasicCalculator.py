def add() :
    num1 = input("Enter a number")
    num2 = input("Enter a number to add")
    answer_add = float(num1) + float(num2)
    print(answer_add)
def subtract() :
    num3 = input("Enter a number")
    num4 = input( "Enter another numbe to subtract")
    answer_subtract = float(num3) - float(num4)
    print(answer_subtract) 
def multiply():
    num5 = input("Enter a number")
    num6 = input("Enter another number to multiply")
    answer_multiply = float(num5) * float(num6)
    print(answer_multiply)
def divide():
    num7 = input("Enter a number")
    num8 = input("Enter another number to divide")
    answer_divide = float(num7) / float(num8)
    print(answer_divide)
ask = input("Do u want to add, subtract, divide or multiply? ")
if ask == "add" :
    add()
elif ask =="subtract" :
    subtract()
elif ask =="multiply" :
    multiply()
elif ask == "divide":
    divide()
