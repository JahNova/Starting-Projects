#define functions
def inputs():
   name = input("Name: ")
   gender = input("Gender: ").lower()
   age = input("Age: ")
   return (name, gender, age)

def phrase(name, gender, age):
   phrase = (f"""There once was a {gender} named {name}.
            He was {age} years old.
            He really liked the name {name}
            but didn't like being {age} years old.""")
   if gender == "male":
       print(phrase)
   elif gender == "female":
       print(phrase.replace('He', 'She'))
   else:
       #rudimentary error checking
       print("Unrecognized notation for subject {gender}")

def main():
   name, gender, age = inputs()
   phrase(name, gender, age)

main()   
