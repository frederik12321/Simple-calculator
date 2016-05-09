print("This is a very simple calculator")
print("The possible options are + - * /")

First_number = int(input("Enter your first number:"))

Transaction = str(input("Enter + - * /:  "))

while Transaction != "+" and Transaction != "-" and Transaction != "*" and Transaction != "/" :
        print("Calculation is not possible")
        Transaction = str(input("Enter + - * /:  "))

Second_number = int(input("Enter your second number:"))


Solution = 0

if Transaction == "+":
    Solution = First_number + Second_number

if Transaction == "-":
    Solution = First_number - Second_number

if Transaction == "*":
    Solution = First_number * Second_number

if Transaction == "/":
    Solution = First_number / Second_number

print("This is the solution: ", Solution)

