class Index:
   selected_patient = {}
   patient1 = {"name": "John", "age": 37, "weight": 182}
   patient2 = {"name": "Alex", "age": 23, "weight": 135}

   @classmethod
   def select_patient(cls):
       while True:
           #select patient 1 or 2
           sel = int(input("Choose: "))
           if sel == 1:
               cls.selected_patient = cls.patient1
               break
           elif sel == 2:
               cls.selected_patient = cls.patient2
               break
             
   @classmethod
   def get_info(cls):
       while True:
           #select patient information
           info = input("Info: ")
           if info == "name":
               print("Name:", cls.selected_patient["name"])
           elif info == "age":
               print("Age:", cls.selected_patient["age"])
           elif info == "weight":
               print("Weight:", cls.selected_patient["weight"])
           elif info == "back":
               break
           elif info == "quit":
               return (info)
             
def main():
   #gui
   print("Commands: quit | back")
   
  #condition for program to run
   x = "continue"
   while x == "continue":
       Index.select_patient()
       y = Index.get_info()
       #condition to end program
       if y == "quit":
           x = "End"
   print("Closing Patient Index")

main()
