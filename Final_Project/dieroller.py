from tkinter import *
from tkinter import ttk
import dice2
import saving

# Start up
root = Tk()
root.title("D&D Dice Roller (Test)")

# Roots minimum size
root.minsize(500, 250)

# Display
frame_w_d = int(root.winfo_width() * 0.33)
frame_h_d = int(root.winfo_height() * 0.9)
frame_w_b = int(root.winfo_width())
frame_h_b = int(root.winfo_height() * 0.1)
frame1 = Frame(root, width=frame_w_d, height=frame_h_d, relief="solid")
frame2 = Frame(root, width=frame_w_d, height=frame_h_d, relief="solid")
frame3 = Frame(root, width=frame_w_d, height=frame_h_d, relief="solid")
frame4 = Frame(root, width=frame_w_b, height=frame_h_b, relief="solid")

frame1.pack(side=LEFT, fill=BOTH, expand=True)
frame2.pack(side=LEFT, fill=BOTH, expand=True)
frame3.pack(side=LEFT, fill=BOTH, expand=True)
frame4.pack(side=BOTTOM, fill=BOTH, expand=True)

# frame1.grid(row=0, column=0)
# frame2.grid(row=0, column=1)
# frame3.grid(row=0, column=3)
# frame4.grid(row=1, column=0, columnspan=3)

# Dice d4
frame_d4 = Frame(frame1, relief="solid")
die_amount_label_d4 = Label(frame_d4, text="Enter the number of dice:")
die_amount_label_d4.grid(row=0, column=0, padx=10, pady=10, sticky=W)
die_amount_entry_d4 = Entry(frame_d4)
die_amount_entry_d4.grid(row=0, column=1, padx=10, pady=10)
roll_button_d4 = Button(frame_d4, text="Roll", command=lambda: roll_dice(4))
roll_button_d4.grid(row=0, column=2, padx=10, pady=10)
rolls_label_d4 = Label(frame_d4, text="Rolls:")
rolls_label_d4.grid(row=1, column=0, padx=10, pady=10, sticky=W)
rolls_listbox_d4 = Listbox(frame_d4)
rolls_listbox_d4.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)
sum_label_d4 = Label(frame_d4, text="Sum:")
sum_label_d4.grid(row=3, column=0, padx=10, pady=10, sticky=W)
sum_value_label_d4 = Label(frame_d4, text="0")
sum_value_label_d4.grid(row=3, column=1, padx=10, pady=10)
clear_button_d4 = Button(frame_d4, text="Clear", command=lambda: clear_rolls(4))
clear_button_d4.grid(row=3, column=2, padx=10, pady=10)
frame_d4.pack(fill=BOTH, expand=True)

# Dice d8
frame_d8 = Frame(frame1, relief="solid")
die_amount_label_d8 = Label(frame_d8, text="Enter the number of dice:")
die_amount_label_d8.grid(row=0, column=0, padx=10, pady=10, sticky=W)
die_amount_entry_d8 = Entry(frame_d8)
die_amount_entry_d8.grid(row=0, column=1, padx=10, pady=10)
roll_button_d8 = Button(frame_d8, text="Roll", command=lambda: roll_dice(8))
roll_button_d8.grid(row=0, column=2, padx=10, pady=10)
rolls_label_d8 = Label(frame_d8, text="Rolls:")
rolls_label_d8.grid(row=1, column=0, padx=10, pady=10, sticky=W)
rolls_listbox_d8 = Listbox(frame_d8)
rolls_listbox_d8.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)
sum_label_d8 = Label(frame_d8, text="Sum:")
sum_label_d8.grid(row=3, column=0, padx=10, pady=10, sticky=W)
sum_value_label_d8 = Label(frame_d8, text="0")
sum_value_label_d8.grid(row=3, column=1, padx=10, pady=10)
clear_button_d8 = Button(frame_d8, text="Clear", command=lambda: clear_rolls(8))
clear_button_d8.grid(row=3, column=2, padx=10, pady=10)
frame_d8.pack(fill=BOTH, expand=True)

# Dice d12
frame_d12 = Frame(frame1, relief="solid")
die_amount_label_d12 = Label(frame_d12, text="Enter the number of dice:")
die_amount_label_d12.grid(row=0, column=0, padx=10, pady=10, sticky=W)
die_amount_entry_d12 = Entry(frame_d12)
die_amount_entry_d12.grid(row=0, column=1, padx=10, pady=10)
roll_button_d12 = Button(frame_d12, text="Roll", command=lambda: roll_dice(12))
roll_button_d12.grid(row=0, column=2, padx=10, pady=10)
rolls_label_d12 = Label(frame_d12, text="Rolls:")
rolls_label_d12.grid(row=1, column=0, padx=10, pady=10, sticky=W)
rolls_listbox_d12 = Listbox(frame_d12)
rolls_listbox_d12.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)
sum_label_d12 = Label(frame_d12, text="Sum:")
sum_label_d12.grid(row=3, column=0, padx=10, pady=10, sticky=W)
sum_value_label_d12 = Label(frame_d12, text="0")
sum_value_label_d12.grid(row=3, column=1, padx=10, pady=10)
clear_button_d12 = Button(frame_d12, text="Clear", command=lambda: clear_rolls(12))
clear_button_d12.grid(row=3, column=2, padx=10, pady=10)
frame_d12.pack(fill=BOTH, expand=True)

# Dice d20
frame_d20 = Frame(frame2, relief="solid")
die_amount_label_d20 = Label(frame_d20, text="Enter the number of dice:")
die_amount_label_d20.grid(row=0, column=0, padx=10, pady=10, sticky=W)
die_amount_entry_d20 = Entry(frame_d20)
die_amount_entry_d20.grid(row=0, column=1, padx=10, pady=10)
roll_button_d20 = Button(frame_d20, text="Roll", command=lambda: roll_dice(20))
roll_button_d20.grid(row=0, column=2, padx=10, pady=10)
rolls_label_d20 = Label(frame_d20, text="Rolls:")
rolls_label_d20.grid(row=1, column=0, padx=10, pady=10, sticky=W)
rolls_listbox_d20 = Listbox(frame_d20)
rolls_listbox_d20.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)
sum_label_d20 = Label(frame_d20, text="Sum:")
sum_label_d20.grid(row=3, column=0, padx=10, pady=10, sticky=W)
sum_value_label_d20 = Label(frame_d20, text="0")
sum_value_label_d20.grid(row=3, column=1, padx=10, pady=10)
clear_button_d20 = Button(frame_d20, text="Clear", command=lambda: clear_rolls(20))
clear_button_d20.grid(row=3, column=2, padx=10, pady=10)
frame_d20.pack(fill=BOTH, expand=True)

# Dice d6
frame_d6 = Frame(frame2, relief="solid")
die_amount_label_d6 = Label(frame_d6, text="Enter the number of dice:")
die_amount_label_d6.grid(row=0, column=0, padx=10, pady=10, sticky=W)
die_amount_entry_d6 = Entry(frame_d6)
die_amount_entry_d6.grid(row=0, column=1, padx=10, pady=10)
roll_button_d6 = Button(frame_d6, text="Roll", command=lambda: roll_dice(6))
roll_button_d6.grid(row=0, column=2, padx=10, pady=10)
rolls_label_d6 = Label(frame_d6, text="Rolls:")
rolls_label_d6.grid(row=1, column=0, padx=10, pady=10, sticky=W)
rolls_listbox_d6 = Listbox(frame_d6)
rolls_listbox_d6.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)
sum_label_d6 = Label(frame_d6, text="Sum:")
sum_label_d6.grid(row=3, column=0, padx=10, pady=10, sticky=W)
sum_value_label_d6 = Label(frame_d6, text="0")
sum_value_label_d6.grid(row=3, column=1, padx=10, pady=10)
clear_button_d6 = Button(frame_d6, text="Clear", command=lambda: clear_rolls(6))
clear_button_d6.grid(row=3, column=2, padx=10, pady=10)
frame_d6.pack(fill=BOTH, expand=True)

# Dice d10
frame_d10 = Frame(frame3, relief="solid")
die_amount_label_d10 = Label(frame_d10, text="Enter the number of dice:")
die_amount_label_d10.grid(row=0, column=0, padx=10, pady=10, sticky=W)
die_amount_entry_d10 = Entry(frame_d10)
die_amount_entry_d10.grid(row=0, column=1, padx=10, pady=10)
roll_button_d10 = Button(frame_d10, text="Roll", command=lambda: roll_dice(10))
roll_button_d10.grid(row=0, column=2, padx=10, pady=10)
rolls_label_d10 = Label(frame_d10, text="Rolls:")
rolls_label_d10.grid(row=1, column=0, padx=10, pady=10, sticky=W)
rolls_listbox_d10 = Listbox(frame_d10)
rolls_listbox_d10.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)
sum_label_d10 = Label(frame_d10, text="Sum:")
sum_label_d10.grid(row=3, column=0, padx=10, pady=10, sticky=W)
sum_value_label_d10 = Label(frame_d10, text="0")
sum_value_label_d10.grid(row=3, column=1, padx=10, pady=10)
clear_button_d10 = Button(frame_d10, text="Clear", command=lambda: clear_rolls(10))
clear_button_d10.grid(row=3, column=2, padx=10, pady=10)
frame_d10.pack(fill=BOTH, expand=True)

# Dice d100
frame_d100 = Frame(frame3, relief="solid")
die_amount_label_d100 = Label(frame_d100, text="Enter the number of dice:")
die_amount_label_d100.grid(row=0, column=0, padx=10, pady=10, sticky=W)
die_amount_entry_d100 = Entry(frame_d100)
die_amount_entry_d100.grid(row=0, column=1, padx=10, pady=10)
roll_button_d100 = Button(frame_d100, text="Roll", command=lambda: roll_dice(100))
roll_button_d100.grid(row=0, column=2, padx=10, pady=10)
rolls_label_d100 = Label(frame_d100, text="Rolls:")
rolls_label_d100.grid(row=1, column=0, padx=10, pady=10, sticky=W)
rolls_listbox_d100 = Listbox(frame_d100)
rolls_listbox_d100.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)
sum_label_d100 = Label(frame_d100, text="Sum:")
sum_label_d100.grid(row=3, column=0, padx=10, pady=10, sticky=W)
sum_value_label_d100 = Label(frame_d100, text="0")
sum_value_label_d100.grid(row=3, column=1, padx=10, pady=10)
clear_button_d100 = Button(frame_d100, text="Clear", command=lambda: clear_rolls(100))
clear_button_d100.grid(row=3, column=2, padx=10, pady=10)
frame_d100.pack(fill=BOTH, expand=True)

# Dice d1
frame_d1 = Frame(frame3, relief="solid")
die_amount_label_d1 = Label(frame_d1, text="Enter the number of dice:")
die_amount_label_d1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
die_amount_entry_d1 = Entry(frame_d1)
die_amount_entry_d1.grid(row=0, column=1, padx=10, pady=10)
num_of_sides_label_d1 = Label(frame_d1, text="Enter the number of sides:")
num_of_sides_label_d1.grid(row=1, column=0, padx=10, pady=10, sticky=W)
num_of_sides_entry = Entry(frame_d1)
num_of_sides_entry.grid(row=1, column=1, padx=10, pady=10)
roll_button_d1 = Button(frame_d1, text="Roll", command=lambda: roll_dice(int(num_of_sides_entry.get())))
roll_button_d1.grid(row=0, rowspan=2, column=2, padx=10, pady=10)
rolls_label_d1 = Label(frame_d1, text="Rolls:")
rolls_label_d1.grid(row=2, column=0, padx=10, pady=10, sticky=W)
rolls_listbox_d1 = Listbox(frame_d1)
rolls_listbox_d1.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky=NSEW)
sum_label_d1 = Label(frame_d1, text="Sum:")
sum_label_d1.grid(row=4, column=0, padx=10, pady=10, sticky=W)
sum_value_label_d1 = Label(frame_d1, text="0")
sum_value_label_d1.grid(row=4, column=1, padx=10, pady=10)
clear_button_d1 = Button(frame_d1, text="Clear", command=lambda: clear_rolls(int(num_of_sides_entry.get())))
clear_button_d1.grid(row=4, column=2, padx=10, pady=10)
frame_d1.pack(fill=BOTH, expand=True)

start_button = Button(frame4, text="Start Session", command=lambda: start_session())
start_button.pack(side=LEFT, padx=10, pady=10)
end_button = Button(frame4, text="End Session", command=lambda: end_session())
end_button.pack(side=LEFT, padx=10, pady=10)
# past_sessions_button = Button(frame4, text="Past Rolls", command= (new window or tab that displays old sessions rolles))
# past_sessions_button.pack(side=LEFT, padx=10, pady=10)

# Dice function
def retrive_data(sides):
    if sides == 20:
        return die_amount_entry_d20.get()
    elif sides == 6:
        return die_amount_entry_d6.get()
    elif sides == 8:
        return die_amount_entry_d8.get()
    elif sides == 4:
        return die_amount_entry_d4.get()
    elif sides == 12:
        return die_amount_entry_d12.get()
    elif sides == 10:
        return die_amount_entry_d10.get()
    elif sides == 100:
        return die_amount_entry_d100.get()
    else:
        return die_amount_entry_d1.get()
    
def send_data(sides, rolls):
    if sides == 20:
        rolls_listbox_d20.insert(0, rolls)
        sum_value_label_d20.config(text=str(dice2.sum_of_rolls(rolls)))
    elif sides == 6:
        rolls_listbox_d6.insert(0, rolls)
        sum_value_label_d6.config(text=str(dice2.sum_of_rolls(rolls)))
    elif sides == 8:
        rolls_listbox_d8.insert(0, rolls)
        sum_value_label_d8.config(text=str(dice2.sum_of_rolls(rolls)))
    elif sides == 4:
        rolls_listbox_d4.insert(0, rolls)
        sum_value_label_d4.config(text=str(dice2.sum_of_rolls(rolls)))
    elif sides == 12:
        rolls_listbox_d12.insert(0, rolls)
        sum_value_label_d12.config(text=str(dice2.sum_of_rolls(rolls)))
    elif sides == 10:
        rolls_listbox_d10.insert(0, rolls)
        sum_value_label_d10.config(text=str(dice2.sum_of_rolls(rolls)))
    elif sides == 100:
        rolls_listbox_d100.insert(0, rolls)
        sum_value_label_d100.config(text=str(dice2.sum_of_rolls(rolls)))
    else:
        rolls_listbox_d1.insert(0, rolls)
        sum_value_label_d1.config(text=str(dice2.sum_of_rolls(rolls)))

def roll_dice(sides):
    die_amount = retrive_data(sides)
    rolls = dice2.roll_x_dice(die_amount, sides)
    send_data(sides, rolls)
    saving.session_storage_update(this_session, rolls, sides)

def clear_rolls(sides):
    if sides == 20:
        rolls_listbox_d20.delete(0, END)
        sum_value_label_d20.config(text="0")
    elif sides == 6:
        rolls_listbox_d6.delete(0, END)
        sum_value_label_d6.config(text="0")
    elif sides == 8:
        rolls_listbox_d8.delete(0, END)
        sum_value_label_d8.config(text="0")
    elif sides == 4:
       rolls_listbox_d4.delete(0, END)
       sum_value_label_d4.config(text="0")
    elif sides == 12:
        rolls_listbox_d12.delete(0, END)
        sum_value_label_d12.config(text="0")
    elif sides == 10:
        rolls_listbox_d10.delete(0, END)
        sum_value_label_d10.config(text="0")
    elif sides == 100:
        rolls_listbox_d100.delete(0, END)
        sum_value_label_d100.config(text="0")
    else:
        rolls_listbox_d1.delete(0, END)
        sum_value_label_d1.config(text="0")

# saving functions
this_session = {}
def start_session():
    global this_session
    this_session.update(saving.session_start())

def end_session():
    saving.session_end(this_session)

root.mainloop()