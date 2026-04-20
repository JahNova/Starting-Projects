# ------------------IMPORTS-----------------
import _tkinter
from tkinter import *
from tkinter import messagebox
import json


# ------------------CONSTANTS-----------------


BUTTON_COLOR = "#b8142f"
WINDOW_COLOR = "#fc8de3"
OUTLINE_COLOR = "#b814b2"
ENTRY_COLOR = "#f5b4fa"
dict_of_stuff = {}
week = "Week1"
week_number = 1






# -------------------------FUNCTIONS-----------------------------




def calculate_total(dict_):
   dict_["Total"] = 0


   # Calculates the total cost of all items in the dictionary
   sum_of_prices = 0
   for old_price in (dict_.values()):
       sum_of_prices += float(old_price)


   # Returns the dictionary with the altered total
   dict_["Total"] = sum_of_prices
   return dict_




def change_week():
   global week, week_number, dict_of_stuff
   week_number = week_entry.get()


   # Error catching
   try:
       int(week_number) / 1
   except ValueError:
       messagebox.showerror(message="Invalid week number!")
       week_entry.delete(0, END)
   else:
       print("Valid number")


       # Changes the value of the global week variable
       week = f"Week{week_number}"
       messagebox.showinfo(message=f"You are now viewing Week {week_number}")
       week_entry.delete(0, END)
       main_window.after(200, reload_file_window)


       with open("list.json") as file:
           dict_of_stuff = json.load(file)[week]




def update_file():
   global week, reborn_text
   with open("list.json") as file:
       updated_info = json.load(file)
       updated_week = {}


       #Converts the items in the file menu into a series of lists
       current_week = reborn_text.get(index1=0.0, index2=END)
       current_week = current_week.split("\n")
       current_week = "   ".join(current_week).strip()
       current_week = current_week.split("   ")


       # Converts the series of lists into a dictionary


       for item in current_week:
           # Catches any error that may result from editing the file in a manner that is incompatible with the program
           try:
               item = item.split(": ")
               updated_week[item[0]] = item[1]
           # Effectively deletes the line that was incorrectly edited
           # If another variable is created, it could simply be that nothing gets changed
           except:
               messagebox.showerror(message="Edit is incompatible with the program")




       # Recalculates the total of the updated dictionary
       updated_info[week] = calculate_total(updated_week)


       # Reloads the file menu window
       main_window.after(200, reload_file_window)


       with open("list.json", "w") as file:
           json.dump(updated_info, file, indent=4)




def reload_file_window():
   global file_window, week, reborn_text, week_number


   try:
       file_window.destroy()
   except _tkinter.TclError:
       pass
   else:
       file_window = Tk()


       reborn_button = Button(file_window, text="Update File", command=update_file)
       reborn_text = Text(file_window)


       reborn_button.pack()
       reborn_text.pack()


       with open("list.json") as file:
           try:
               reloaded_info = json.load(file)[week]


           except KeyError:
               print("Key error caught")
               new_week = {f"Week{week_number}": {}}


               with open("list.json", "r") as file:
                   data = json.load(file)
                   print(data)
                   data.update(new_week)


               with open("list.json", "w") as file:
                   json.dump(data, file, indent=4)
               print("Hello")
               week_entry.delete(0, END)
               main_window.after(200, reload_file_window)


           finally:
               string_ = ""


               try:
                   for product, price in reloaded_info.items():
                       string_ += f"{product}: {price}\n"
               except UnboundLocalError:
                   ...


               reborn_text.insert(chars=string_, index=0.0)




# ----------------------Unused Functions-------------------------




#-------------------Main Function------------------
def insert():
   global dict_of_stuff


   new_product = product_entry.get()
   new_price = price_entry.get()


   # Error catching
   if new_product == "":
       messagebox.showerror(title="Value Error", message="Missing one or more values")


   elif new_price == "":
       messagebox.showerror(title="Value Error", message="Missing one or more values")


   else:


       try:
           float(new_price) / 1
       except TypeError:
           messagebox.showerror(title="Type Error", message="Price must be a number")
           price_entry.delete(0, END)


       else:
           # update_dict(new_product, new_price, dict_of_stuff)


           # Changes the dictionary's total
           try:
               del dict_of_stuff["Total"]


           except KeyError:
               dict_of_stuff["Total"] = 0


           # Adds the new item to the dictionary
           dict_of_stuff[new_product.title()] = new_price


           # Recalculates the dictionaries total
           dict_of_stuff = calculate_total(dict_of_stuff)


           # Edits the json file to add the new information
           with open("list.json", "r") as file:
               data = json.load(file)
               data[week] = dict_of_stuff


           with open("list.json", "w") as file:
               json.dump(data, file, indent=4)


           main_window.after(200, reload_file_window)




# ----------------------------------GUI-----------------------------------
main_window = Tk()
main_window.geometry("200x150")
main_window.title("Update List")
main_window.config(background=WINDOW_COLOR, highlightthickness=10, highlightcolor=OUTLINE_COLOR)


# -----------------File Window-------------------
file_window = Tk()


text = Text(file_window)
button = Button(file_window, text="Update File")


text.pack()
button.pack()


with open("list.json") as file:
   file_info = file.read()
   text.insert(chars=file_info, index=0.0)


# --------------------Labels--------------------
product_label = Label(main_window, text="Product:", bg=WINDOW_COLOR)
price_label = Label(main_window, text="Price:", bg=WINDOW_COLOR)
place_holder = Label(main_window)


# --------------------Entry Boxes--------------------
product_entry = Entry(main_window)
price_entry = Entry(main_window)
week_entry = Entry(main_window, width=5)


product_entry.insert(index=0, string="Charger")
price_entry.insert(index=0, string="15")


# -------------------Buttons-------------------
insert_button = Button(main_window, text="Insert Item", command=insert, bg=BUTTON_COLOR)
file_button = Button(main_window, text="Open File", command=reload_file_window, bg=BUTTON_COLOR)
week_button = Button(main_window, text="Change Week", command=change_week, bg=BUTTON_COLOR)


# ------------------------Grid----------------------
product_label.grid(column=0, row=0)
price_label.grid(column=0, row=1)


product_entry.grid(column=1, row=0)
price_entry.grid(column=1, row=1)


insert_button.grid(column=1, row=2)
file_button.grid(column=1, row=3)


week_entry.grid(column=1, row=5, columnspan=1)
week_button.grid(column=1, row=4, columnspan=1)


main_window.mainloop()

