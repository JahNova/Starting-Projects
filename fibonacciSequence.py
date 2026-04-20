current_num = 0
next_num = 1
# print("\n----------------------\n1st in line:",current_num)
# print(f"2nd in line: {next_num}\n----------------------\n")

choice = input("How Many Numbers Do you Wish to Print?: ")

x = 0
while x < int(choice):
   sum = int(current_num) + int(next_num)
   print("Sum:", sum)

   current_num = next_num
   # print("\n----------------------\n1st in line:",current_num)
   next_num = sum
   # print(f"2nd in line: {next_num}\n----------------------\n")
   x += 1
