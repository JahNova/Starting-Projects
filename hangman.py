def get_letter():
   #user guesses a letter
   letter = input("Guess: ")
  
   #must only be one letter
   while len(letter) > 1:
       print("ONLY TYPE ONE LETTER")
       letter = input("Guess: ")
   return letter

def check_letter(letter):
   global restricted_letters
   global struc
   global guess_limit
   global word

   #ensure no repeated letters
   if letter in restricted_letters:
       print("YOU'VE ALREADY GUESSED THAT LETTER ")
       print(struc)
   else:
       #checks if the guess present in the secret word
       if word.find(letter) >= 0:
           print("CORRECT")
         
           #replaces the placeholders with correctly guessed letters
           for i in range(len(word)):
               if word[i] == letter:
                   struc.pop(i)
                   struc.insert(i, letter)
           restricted_letters += letter
           print(struc)
           print(word)
       else:
           print("INCORRECT")
           guess_limit -= 1
           print(struc)
           restricted_letters += letter

def main():
   #set conditions for program to run
   while guess_limit > 0 and "_" in struc:
       letter = get_letter()
       check_letter(letter)
   print("YOU WIN")

word = "flla"
guess_limit = 10
letter = "o"
struc = ["_", "_", "_", "_"]
restricted_letters = []

main()


