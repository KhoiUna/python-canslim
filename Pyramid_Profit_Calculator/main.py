from tkinter import *
from pyramid_string import pyramid_string


def compute():
    initial = float(myInitialString.get())
    price = float(myCurrentPriceString.get())
    tp = round(price * 1.2, 2)

    myTakeProfitString.set(str(tp))
    string = pyramid_string(initial, price)
    myLabel5.config(text=string)


# Window:
window = Tk()
window.title("Pyramid Calculator")
window.minsize(400, 300)
window.configure(bg="grey")

# Labels
myLabel1 = Label(window, text="Initial:", fg="black")
myLabel1.grid(row=0, column=0, padx=0, pady=10)

myLabel2 = Label(window, text="Current Price:", fg="black")
myLabel2.grid(row=1, column=0, padx=10, pady=10)

myLabel3 = Label(window, text="TP:", fg="black")
myLabel3.grid(row=3, column=0, padx=0, pady=10)

myLabel4 = Label(window, text="-----PYRAMID-----", fg="black")
myLabel4.grid(row=4, column=1, padx=10, pady=15)

myLabel5 = Label(window, text='', fg="black")
myLabel5.grid(row=5, column=0, padx=10, pady=15, columnspan=3)

# Entries
myInitialString = StringVar()
myInitial = Entry(window, textvariable=myInitialString, width=15)
myInitial.grid(row=0, column=2)

myCurrentPriceString = StringVar()
myCurrentPrice = Entry(window, textvariable=myCurrentPriceString, width=15)
myCurrentPrice.grid(row=1, column=2)

myTakeProfitString = StringVar()
myTakeProfit = Entry(window, state='readonly',
                     textvariable=myTakeProfitString, width=15)
myTakeProfit.grid(row=3, column=2)

# Compute Button
myButton = Button(window, text="CALCULATE",
                  bg="light green", command=compute)
myButton.grid(row=2, column=1, padx=10, pady=15)

# Mainloop:
window.mainloop()
