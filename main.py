from tkinter import *
window = Tk()
window.title("The Converter")
window.minsize(width=300, height=230)
window.config(padx=25, pady=25, background="#f5deb3")


def mi_to_km(number):
    return number * 1.609


def km_to_mi(number):
    return number / 1.609


def f_to_c(number):
    return (number - 32) * 5/9


def c_to_f(number):
    return (number * 9/5) + 32


# Listbox
def listbox_used():
    number = float(entry.get())
    selection = listbox.index(listbox.curselection())
    if selection == 0:
        answer = mi_to_km(number)
        label_ans.config(text=round(answer, 2))
    elif selection == 1:
        answer = km_to_mi(number)
        label_ans.config(text=round(answer, 2))
    elif selection == 2:
        answer = f_to_c(number)
        label_ans.config(text=round(answer, 2))
    else:
        answer = c_to_f(number)
        label_ans.config(text=round(answer, 2))


# Labels
label_func = Label(text="Select function:")
label_func.config(pady=10, background="#f5deb3")
label_func.grid(row=1, column=1)

# Labels
label_num = Label(text="Select Number:")
label_num.config(pady=1, background="#f5deb3")
label_num.grid(row=1, column=2)

# Labels
label_conv = Label(text="Conversion:")
label_conv.config(pady=1, background="#f5deb3")
label_conv.grid(row=3, column=2)

# Labels
label_ans = Label(text="0", width=10)
label_ans.config(pady=1, background="white")
label_ans.grid(row=3, column=3)

listbox = Listbox(height=4, width=7)
options = ["mi to km", "km to mi", "(F) to (C)", "(C) to (F)"]
for item in options:
    listbox.insert(options.index(item), item)
listbox.bind("<<ListboxSelect>>")

listbox.grid(row=2, column=1)

# Entries
entry = Entry(width=10, borderwidth=0, relief=FLAT)
entry.insert(END, string="0")
entry.grid(row=1, column=3)


button = Button(text="Convert", command=listbox_used, bg="#f5deb3")
button.grid(row=2, column=3)














window.mainloop()