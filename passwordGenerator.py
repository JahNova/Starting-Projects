from random import randint

def change_vowels(site):
   for i in site.lower():
       if i in ("aeiou"):
           if i == "a":
               i = i.replace(i, "e")
               password.append(i)
             
           elif i == "e":
               i = i.replace(i, "i")
               password.append(i)
             
           elif i == "i":
               i = i.replace(i, "o")
               password.append(i)

           elif i == "o":
               i = i.replace(i, "u")
               password.append(i)

           elif i == "u":
               i = i.replace(i, "a")
               password.append(i)
       else:
           password.append(i)

   return len(password)

def first_number():
   num = len(password)
   password.append(str(num))

def second_number():
   num2 = 0
   for letter in password:
       if letter in ("aeiou"):
           num2 += 1
   password.append(str(num2))
   return (num2)

def third_number():
   x = 1
   while x == 1:
       num3 = randint(1, 9)
       if int(num2) + int(num3) == password_len:
           x = 0
           password.append(str(num3))

def special_characters():
   global password
   password = " ".join(password)
   for y in password:
       if y in "a":
           password = password.replace(y, "@")


   password = password.split(" ")
   print(password)

def special_characters2():
   global password
   for z in password:
       if z in "1234567890":
           if z == "1":
               password.append("!")

           elif z == "2":
               password.append("@")

           elif z == "3":
               password.append("#")

           elif z == "4":
               password.append("$")

           elif z == "5":
               password.append("%")

           elif z == "6":
               password.append("^")

           elif z == "7":
               password.append("&")

           elif z == "8":
               password.append("*")

           elif z == "9":
               password.append("(")

           elif z == "0":
               password.append(")")

password = []


site = input("Site: ")

# changes every vowel one space over
password_len = change_vowels(site)


# the 1st number is the number of letters in the site name
first_number()

# the 2nd number is the number of vowels in the site name
num2 = second_number()

# the 3rd number is the number of letters in the site minus the number of vowels
third_number()

# changes "a" to "@"
special_characters()

special_characters2()


password = "".join(password)
print(password)
