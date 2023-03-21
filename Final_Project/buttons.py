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
