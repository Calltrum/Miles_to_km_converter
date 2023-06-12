from tkinter import *

window = Tk()
window.title('Miles To Km Converter')
window.minsize(width=400, height=150)
window.config(padx=20, pady=20)


def miles_to_km():
    mile = float(input.get())
    result = round(mile * 1.60934)
    km_variable.config(text=result)


input = Entry(width=8)
input.place(x=150, y=20)

miles = Label(text='Miles')
miles.place(x=200, y=20)
miles.config(pady=0, padx=20)

is_equal_to = Label(text='is equal to ')
is_equal_to.place(x=80, y=50)

km_variable = Label(text=0)
km_variable.place(x=170, y=50)

km_label = Label(text='Km')
km_label.place(x=220, y=50)

calc_button = Button(text='Calculate', command=miles_to_km)
calc_button.place(x=150, y=80)
window.mainloop()
