import pandas
from math import ceil, floor
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt






def get_percentile():
   try:
       percentile = int(kth_percentile.get())
       if percentile < 10 or percentile > 90:
           messagebox.showerror(message="Pick a number between 10 and 90")
       else:
           result = calc_percentile(kth_percentile.get())
           messagebox.showinfo(message=f"The number represented by the {percentile}th percentile is {result}")


   except ValueError:
       messagebox.showerror(message="Pick a number between 10 and 90")
   finally:
       kth_percentile.delete(0, END)




def submit_list():
   global list_


   try:
       list_ = sorted(data_frame[enter_list.get()].to_list())
       int(list_[0]) + int(list_[1])
   except KeyError:
       messagebox.showwarning(message="Invalid column name")
   except ValueError:
       messagebox.showwarning(message="Column must only contain numbers")
   else:
       math_stuff.grid(column=1, row=1)
       messagebox.showinfo(message=f"The column in use has been set to: {enter_list.get()}")
   finally:
       enter_list.delete(0,END)




def calc_frequency():
   global list_


   no_repeats = []
   for i in list_:
       if i not in no_repeats:
           no_repeats.append(i)


   no_repeats = sorted(no_repeats)


   frequency = []
   for number in no_repeats:
       frequency.append(list_.count(number))


   dataframe = pandas.DataFrame({
       'Class': [i for i in no_repeats],
       'Frequency': frequency
   })


   values = dataframe['Class'].to_list()
   frequencies = dataframe['Frequency'].to_list()


   plt.bar(values, frequencies, width=.7)
   plt.xlabel('Values')
   plt.ylabel('Frequencies')
   plt.title('Frequency Chart')
   plt.show()


def calc_summary_values():
   global list_


   minimum = list_[0]
   maximum = max(list_)
   summary_values = ["Minimum: " + str(minimum), "1st Percentile: " + str(calc_percentile(25)),
                     "Median: " + str(calc_percentile(50)), "3rd Percentile: " + str(calc_percentile(75)),
                     "Maximum: " + str(maximum)]
   messagebox.showinfo(message='\n'.join(summary_values))




def calc_percentile(x):
   global list_


   result = (int(x) / 100) * (len(list_) + 1)
   if result - int(result) != 0:
       return (list_[ceil(result) - 1] + list_[floor(result) - 1]) / 2
   else:
       return list_[int(result) - 1]




# ---------------------------------VARIABLES---------------------------------
data_set = {
   'Names': ['Carl', 'James', 'Marco', 'Alex', 'May', 'June', 'Holly', 'Daniel', 'Richard', 'Nick'],
   'Ages': [15, 15, 16, 14, 15, 15, 16, 16, 15, 15],
   'Grades': [83, 91, 72, 98, 63, 77, 85, 90, 81, 90]
}


data_frame = pandas.DataFrame(data_set)


WINDOW_BG = "#22adf2"
BUTTON_COLOR = "#5ce2fa"
PAD_X = 10
columns = [i for i in data_frame.columns]
columns = (", ").join(columns)


# ---------------------------------GUI---------------------------------


window = Tk()
window.config(bg=WINDOW_BG)
window.geometry('350x150')


math_stuff = Frame(bg=WINDOW_BG, pady=10)
gui_stuff = Frame(bg=WINDOW_BG)


display_columns = Label(gui_stuff, text=f"Pick a column: {columns}", bg=WINDOW_BG, pady=10)


display_columns.grid(column=0, row=0, columnspan=3)


enter_list = Entry(gui_stuff)
enter_list.grid(column=1, row=1)
enter_list.focus()


change_list = Button(gui_stuff, width=5, text="Submit", bg=BUTTON_COLOR, command=submit_list)
change_list.grid(column=2, row=1)


# ----------------buttons-------------------




frequency_button = Button(math_stuff, text='Frequency Table', command=calc_frequency, bg=BUTTON_COLOR, padx=PAD_X)
frequency_button.grid(column=0, row=0)


summary_values_button = Button(math_stuff, text='Summary Values', command=calc_summary_values, bg=BUTTON_COLOR,
                              padx=PAD_X)
summary_values_button.grid(column=1, row=0)


percentile_button = Button(math_stuff, text='Percentile', command=get_percentile, bg=BUTTON_COLOR, padx=PAD_X)
percentile_button.grid(column=2, row=0)


kth_percentile = Entry(math_stuff, width=10)
kth_percentile.grid(column=2, row=1)


gui_stuff.grid(column=1, row=0)


window.mainloop()


# frequency_table = calc_frequency(numbers_list)
# median = calc_percentile(numbers_list, 25)
# print(pandas.DataFrame(frequency_table))

