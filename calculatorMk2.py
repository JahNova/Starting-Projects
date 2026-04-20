#print gui
print('Operations: + = Addition   - = Subtraction   x = Multiplication   / = Division')

#define functions
def add(num_1,num_2):
   return int(num_1)+int(num_2)
def sub(num_1,num_2):
   return int(num_1)-int(num_2)
def div(num_1,num_2):
   return int(num_1)/int(num_2)
def mult(num_1,num_2):
   return int(num_1)*int(num_2)

#inputs
num_1=input("1st Number: ")
num_2=input("2nd Number: ")
op=input('Choose an operation: ')

#calculations
if op=='+':
   ans=add(num_1,num_2)
   print(ans)
if op=='-':
   ans=sub(num_1,num_2)
   print(ans)
if op=='x':
   ans=mult(num_1,num_2)
   print(ans)
if op=='/':
   ans=div(num_1,num_2)
   print(ans)
