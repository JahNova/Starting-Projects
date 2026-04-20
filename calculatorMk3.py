class Calculator:
   def __init__(self, operator, num1, num2):
       self.operator = operator
       self.num1 = num1
       self.num2 = num2

   def addition(self):
       ans = int(self.num1) + int(self.num2)
       print(ans)

   def subtraction(self):
       ans = int(self.num1) - int(self.num2)
       print(ans)

   def multiplication(self):
       ans = int(self.num1) * int(self.num2)
       print(ans)

   def division(self):
       ans = int(self.num1) / int(self.num2)
       print(ans)

#take inputs
operator = input("Operation: ")
num1 = input("Number: ")
num2 = input("Number: ")

#instantiate calculator object
calculator = Calculator(operator, num1, num2)

#calculate
if operator == "+":
   calculator.addition()

if operator == "-":
   calculator.subtraction()

if operator == "*":
   calculator.multiplication()

if operator == "/":
   calculator.division()
