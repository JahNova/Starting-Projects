from math import *

#print gui
print('Operations: + = Addition   - = Subtraction   x = Multiplication   / = Division   ^ = Exponent   sq = Square root')

#inputs
first = input('First Number: ')
operator = input('Operation: ')
second = input('Second Number: ')

#calculation
if operator=='-':
   ans=float(first) - float(second)
   print('Answer: ' + str(ans))
if operator=='+':
   sum=float(first) + float(second)
   print('Answer: ' + str(sum))
if operator=='/':
   quotient=float(first)/float(second)
   print('Answer: ' + str(quotient))
if operator=='x':
   product=float(first)*float(second)
   print('Answer: ' + str(product))
if operator=='^':
   ans1=float(first)**float(second)
   print('Answer: ' + str(ans2))
if operator=='sq':
   ans2=(float(second)**(1/float(first)))
   print(ans2)
