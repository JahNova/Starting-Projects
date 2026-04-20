from math import pow




def binary_converter(number):
   place = 6
   binary = []


   for i in range(place + 1):
       digit = 0
       current_bit = pow(2, place)


       if number - current_bit >= 0:
           digit = 1
           number -= current_bit
       else:
           digit = 0


       binary.append(digit)
       place -= 1


   print("Binary: ", end="")
   return binary




number = 73
binary_code = binary_converter(number)
print(*binary_code)


bits = 0
for i in binary_code:
   if i == 1:
       bits += 1
print(bits, "Bits")

