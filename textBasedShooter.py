import random


class Rifle:
   magazine = 10

   def shoot(cls):
       shots = input("How many times would you like to fire?: ")
       if int(shots) > cls.magazine:
           print("You don't have enough ammo")
       else:
           if cls.magazine == 0:
               print("You must reload")
           else:
               for i in range(int(shots)):
                   if cls.magazine != 0:
                       cls.magazine -= 1
               print("Bullets Remaining:", cls.magazine)
               return shots
       print("Bullets Remaining:", cls.magazine)

   def reload(cls):
       cls.magazine = 10

def enemies(shots):
   chances = ["You hit an enemy!", "You missed!"]
   for _ in range(int(shots)):
       print(f"{random.choice(chances)}")

def main():
   M14 = Rifle()
   while True:
       action = input("Choose an action: ")
       if action == "s":
           shots = M14.shoot()
           enemies(shots)
       elif action == "r":
           M14.reload()

main()
