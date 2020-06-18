# logarithm calculator using datatype
import math
logg = int
logg = input("log calculation: ")
base = int
base = input("base: ")
print math.log(logg, base)
# calculator using datatype, functions, and dictionaries
n1 = float
n1 = input("n1: ")
n2 = float
n2 = input("n2: ")
def add(n1, n2): return n1 + n2
def sub(n1, n2): return n1 - n2
def mul(n1, n2): return n1 * n2
def div(n1, n2): return n1 / n2
op = {"+": add, "-": sub, "*": mul, "/": div}
op = input("op: ")
print(op(n1, n2))
# calculator using conditions and loop
calculator using conditions
yesno = str
yesno = raw_input("do you wanna use this calculator: ") 
while yesno == "yes":
    num1 = float
    num1 = input("num1: ")
    oper = raw_input("oper: ")
    num2 = float
    num2 = input("num2: ")
    if oper == "+":
        print (num1 + num2)
    if oper == "-":
        print (num1 - num2)
    if oper == "*":
        print (num1 * num2)
    if oper == "/":
        print (num1 / num2)
    yesno = raw_input("do you wanna use this calculator: ")
else:
    print ("power off")