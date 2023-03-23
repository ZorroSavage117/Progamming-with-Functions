from tkinter import *
from tkinter import ttk
import datetime
import dice2
import saving

# Start up
root = Tk()
root.title("D&D Dice Roller (V1.0)")

this_session = {}
this_session.update(saving.session_start())
CURRENT_DATE = datetime.date.today().strftime("%Y-%m-%d")

# Roots minimum size
root.minsize(500, 250)

# Display
frame_w_d = int(root.winfo_width() * 0.33)
frame_h_d = int(root.winfo_height() * 0.9)
frame1 = Frame(root, width=frame_w_d, height=frame_h_d, relief="solid")
frame2 = Frame(root, width=frame_w_d, height=frame_h_d, relief="solid")
frame3 = Frame(root, width=frame_w_d, height=frame_h_d, relief="solid")

frame1.pack(side=LEFT, fill=BOTH, expand=True)
frame2.pack(side=LEFT, fill=BOTH, expand=True)
frame3.pack(side=LEFT, fill=BOTH, expand=True)

# Dice d4
frame_d4 = LabelFrame(frame1, text="D4", relief="solid")
die_amount_label_d4 = Label(frame_d4, text="Enter the number of dice:")
die_amount_label_d4.grid(row=0, column=0, padx=1, pady=1, sticky=W)
die_amount_entry_d4 = Entry(frame_d4)
die_amount_entry_d4.grid(row=0, column=1, padx=1, pady=1)
roll_button_d4 = Button(frame_d4, text="Roll", command=lambda: roll_dice(4))
roll_button_d4.grid(row=0, column=2, padx=1, pady=1)
frame_d4.pack(fill=BOTH, expand=True)

# Dice d8
frame_d8 = LabelFrame(frame1, text="D8", relief="solid")
die_amount_label_d8 = Label(frame_d8, text="Enter the number of dice:")
die_amount_label_d8.grid(row=0, column=0, padx=1, pady=1, sticky=W)
die_amount_entry_d8 = Entry(frame_d8)
die_amount_entry_d8.grid(row=0, column=1, padx=1, pady=1)
roll_button_d8 = Button(frame_d8, text="Roll", command=lambda: roll_dice(8))
roll_button_d8.grid(row=0, column=2, padx=1, pady=1)
frame_d8.pack(fill=BOTH, expand=True)

# Dice d12
frame_d12 = LabelFrame(frame1, text="D12", relief="solid")
die_amount_label_d12 = Label(frame_d12, text="Enter the number of dice:")
die_amount_label_d12.grid(row=0, column=0, padx=1, pady=1, sticky=W)
die_amount_entry_d12 = Entry(frame_d12)
die_amount_entry_d12.grid(row=0, column=1, padx=1, pady=1)
roll_button_d12 = Button(frame_d12, text="Roll", command=lambda: roll_dice(12))
roll_button_d12.grid(row=0, column=2, padx=1, pady=1)
frame_d12.pack(fill=BOTH, expand=True)

# Dice d20
frame_d20 = LabelFrame(frame2, text="D20", relief="solid")
die_amount_label_d20 = Label(frame_d20, text="Enter the number of dice:")
die_amount_label_d20.grid(row=0, column=0, padx=1, pady=1, sticky=W)
die_amount_entry_d20 = Entry(frame_d20)
die_amount_entry_d20.grid(row=0, column=1, padx=1, pady=1)
roll_button_d20 = Button(frame_d20, text="Roll", command=lambda: roll_dice(20))
roll_button_d20.grid(row=0, column=2, padx=1, pady=1)
frame_d20.pack(fill=BOTH, expand=True)

# Output
output_frame = Frame(frame2)
rolls_label = Label(output_frame, text="Rolls:")
rolls_label.grid(row=0, column=0, padx=1, pady=1, sticky=W)
rolls_listbox = Listbox(output_frame)
rolls_listbox.grid(row=1, rowspan=2, column=0, columnspan=1, padx=1, pady=1, sticky=NSEW)
sum_label = Label(output_frame, text="Sum:")
sum_label.grid(row=0, column=1, padx=1, pady=1, sticky=W)
sum_value_label = Label(output_frame, text="0")
sum_value_label.grid(row=1, column=1, padx=1, pady=1)
clear_button = Button(output_frame, text="Clear", command=lambda: clear_rolls())
clear_button.grid(row=2, column=2, padx=1, pady=1)
output_frame.pack(fill=BOTH, expand=True)

# Dice d6
frame_d6 = LabelFrame(frame2, text="D6", relief="solid")
die_amount_label_d6 = Label(frame_d6, text="Enter the number of dice:")
die_amount_label_d6.grid(row=0, column=0, padx=1, pady=1, sticky=W)
die_amount_entry_d6 = Entry(frame_d6)
die_amount_entry_d6.grid(row=0, column=1, padx=1, pady=1)
roll_button_d6 = Button(frame_d6, text="Roll", command=lambda: roll_dice(6))
roll_button_d6.grid(row=0, column=2, padx=1, pady=1)
frame_d6.pack(fill=BOTH, expand=True)

# Dice d10
frame_d10 = LabelFrame(frame3, text="D10", relief="solid")
die_amount_label_d10 = Label(frame_d10, text="Enter the number of dice:")
die_amount_label_d10.grid(row=0, column=0, padx=1, pady=1, sticky=W)
die_amount_entry_d10 = Entry(frame_d10)
die_amount_entry_d10.grid(row=0, column=1, padx=1, pady=1)
roll_button_d10 = Button(frame_d10, text="Roll", command=lambda: roll_dice(10))
roll_button_d10.grid(row=0, column=2, padx=1, pady=1)
frame_d10.pack(fill=BOTH, expand=True)

# Dice d100
frame_d100 = LabelFrame(frame3, text="D100", relief="solid")
die_amount_label_d100 = Label(frame_d100, text="Enter the number of dice:")
die_amount_label_d100.grid(row=0, column=0, padx=1, pady=1, sticky=W)
die_amount_entry_d100 = Entry(frame_d100)
die_amount_entry_d100.grid(row=0, column=1, padx=1, pady=1)
roll_button_d100 = Button(frame_d100, text="Roll", command=lambda: roll_dice(100))
roll_button_d100.grid(row=0, column=2, padx=1, pady=1)
frame_d100.pack(fill=BOTH, expand=True)

# Dice d1
frame_d1 = LabelFrame(frame3, text="D?", relief="solid")
die_amount_label_d1 = Label(frame_d1, text="Enter the number of dice:")
die_amount_label_d1.grid(row=0, column=0, padx=1, pady=1, sticky=W)
die_amount_entry_d1 = Entry(frame_d1)
die_amount_entry_d1.grid(row=0, column=1, padx=1, pady=1)
num_of_sides_label_d1 = Label(frame_d1, text="Enter the number of sides:")
num_of_sides_label_d1.grid(row=1, column=0, padx=1, pady=1, sticky=W)
num_of_sides_entry = Entry(frame_d1)
num_of_sides_entry.grid(row=1, column=1, padx=1, pady=1)
roll_button_d1 = Button(frame_d1, text="Roll", command=lambda: roll_dice(int(num_of_sides_entry.get())))
roll_button_d1.grid(row=0, rowspan=2, column=2, padx=1, pady=1)
frame_d1.pack(fill=BOTH, expand=True)

save_button = Button(frame3, text="Save Session", command=lambda: save_session())
save_button.pack(fill=BOTH, expand=True)
past_button = Button(frame1, text="Past Sessions", command=lambda: past_session())
past_button.pack(fill=BOTH, expand=True)

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
    
def roll_dice(sides):
    global this_session
    die_amount = retrive_data(sides)
    rolls = dice2.roll_x_dice(int(die_amount), sides)
    rolls_listbox.insert(0, rolls)
    sum_value_label.config(text=str(dice2.sum_of_rolls(rolls)))
    saving.session_storage_update(this_session[CURRENT_DATE], rolls, sides)

def clear_rolls():
    rolls_listbox.delete(0, END)
    sum_value_label.config(text="0")

# saving functions
def save_session():
    global this_session
    saving.session_save(this_session)

# past sessions message
def past_session():
    popup = Toplevel(root)

    saves = saving.load_saves()

    message = Message(popup, text=saves)
    message.pack()

root.mainloop()