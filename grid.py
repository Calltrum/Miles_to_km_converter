from tkinter import *

window = Tk()
window.title('Miles To Km Converter')
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)


def miles_to_km():
    mile = float(input.get())
    result = round(mile * 1.60934)
    km_variable.config(text=result)


input = Entry(width=8)
input.grid(column=1, row=0)

miles = Label(text='Miles')
miles.grid(column=2, row=0)
# miles.config(pady=0, padx=20)

is_equal_to = Label(text='is equal to ')
is_equal_to.grid(column=0, row=1)

km_variable = Label(text=0)
km_variable.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

calc_button = Button(text='Calculate', command=miles_to_km)
calc_button.grid(column=1, row=3)
window.mainloop()
