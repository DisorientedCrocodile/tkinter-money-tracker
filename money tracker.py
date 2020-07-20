from tkinter import Tk, Label, Button, Entry, StringVar, X

# Initialization and configuration of window
root = Tk()
root.geometry('300x300')
root.title('Money Tracker')

with open('money.txt', 'r') as f:
    money_lbl = Label(text=f.readline())
    money_lbl.pack(fill=X, expand=True)


def add_value():
    global value_entry
    global money_lbl
    # This checks if what the user entered was a number
    try:
        int(value_entry.get())
    except ValueError as e:
        raise e
    finally:
        pass
    # Gets the number that was stored previously
    with open('money.txt', 'r') as f:
        amt = f.readline()
    # This should erase the contents of the 'money.txt' file
    with open('money.txt', 'w'):
        pass
    # Writing the new value to the file
    with open('money.txt', 'w+') as f:
        new_amt = int(amt) + int(value_entry.get())
        f.write(str(new_amt))
        money_lbl.configure(text=str(new_amt))


def subtract_value():
    global value_entry
    global money_lbl
    # This checks if what the user entered was a number
    try:
        int(value_entry.get())
    except ValueError as e:
        raise e
    finally:
        pass
    # Gets the number that was stored previously
    with open('money.txt', 'r') as f:
        amt = f.readline()
    # This should erase the contents of the 'money.txt' file
    with open('money.txt', 'w'):
        pass
    # Writing the new value to the file
    with open('money.txt', 'w+') as f:
        new_amt = int(amt) - int(value_entry.get())
        f.write(str(new_amt))
        money_lbl.configure(text=str(new_amt))


# Creating a StringVar() for the entry
text_amt = StringVar()

# Person can insert a value in the entry and add or deduct that value from the
# money count using the "Add" or "Deduct" buttons
value_entry = Entry(root, textvariable=text_amt)
value_entry.pack()

add_btn = Button(root, text='Add', command=add_value)
add_btn.pack()

subtract_btn = Button(root, text='Subtract', command=subtract_value)
subtract_btn.pack()

root.mainloop()
