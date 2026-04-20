import time
from tkinter import *


BOX_HEIGHT = 10
BOX_WIDTH = 10
ROW_LENGTH = 10
CURRENT_DAY_COLOR = "#b6f5fc"
OUTLINE_COLOR = "#008efa"


months = {"January": 31, "February": 28, "March": 31, "April": 30, "May":31,"June":30,"July":31}




def get_date():
   time_object = time.localtime()
   month_name = time.strftime("%B", time_object)
   date = time.strftime("%m/%d", time_object)
   month_num = time.strftime("%d")
   return date, month_name, month_num




def determine_days_count(current_month):
   num_of_days = 0
   for key, value in months.items():
       if key == current_month:
           return months[current_month]




def build_calendar(current_day):


   row_ = 1
   column_ = 0
   for day in range(1, num_of_days + 1):
       box = Label(text=f"{day}", width=BOX_WIDTH, height=BOX_HEIGHT, highlightthickness=0,
                   highlightbackground=OUTLINE_COLOR)
       box.grid(row=row_, column=column_)


       if day <= 9:
           box = Label(text=f"0{day}", width=BOX_WIDTH, height=BOX_HEIGHT, highlightthickness=0,
                       highlightbackground=OUTLINE_COLOR)
           box.grid(row=row_, column=column_)


       if box.cget("text") == current_day:
           box.config(bg=CURRENT_DAY_COLOR)
       column_ += 1


       if column_ == ROW_LENGTH:
           row_ += 1
           column_ = 0

current_date, current_month_name, current_day = get_date()
print(current_date)
num_of_days = determine_days_count(current_month_name)


calendar = Tk()


Label(text=f"{current_month_name}",font=('Georgia',40)).grid(row=0, column=0, columnspan=10)




build_calendar(current_day)


calendar.mainloop()

