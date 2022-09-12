# Basic address form using tkinter

import tkinter as tk

window = tk.Tk()
window.title("Address Entry Form")

#------------------------

# Frame 1 - Contains Entry fields
frame_1 = tk.Frame(relief = tk.SUNKEN, borderwidth = 4)
frame_1.grid(row = 0, column = 0)

# First Name
lbl_fname = tk.Label(master = frame_1, text = "First Name:")
lbl_fname.grid(row = 0, column = 0, sticky = "e")
ent_fname = tk.Entry(master = frame_1, width = 50)
ent_fname.grid(row = 0, column = 1)

# Last Name
lbl_lname = tk.Label(master = frame_1, text = "Last Name:")
lbl_lname.grid(row = 1, column = 0, sticky = "e")
ent_lname = tk.Entry(master = frame_1, width = 50)
ent_lname.grid(row = 1, column = 1)

# Address Line 1
lbl_addr1 = tk.Label(master = frame_1, text = "Address Line 1:")
lbl_addr1.grid(row = 2, column = 0, sticky = "e")
ent_addr1 = tk.Entry(master = frame_1, width = 50)
ent_addr1.grid(row = 2, column = 1)

# Address Line 2
lbl_addr2 = tk.Label(master = frame_1, text = "Address Line 2:")
lbl_addr2.grid(row = 3, column = 0, sticky = "e")
ent_addr2 = tk.Entry(master = frame_1, width = 50)
ent_addr2.grid(row = 3, column = 1)

# City
lbl_city = tk.Label(master = frame_1, text = "City:")
lbl_city.grid(row = 4, column = 0, sticky = "e")
ent_city = tk.Entry(master = frame_1, width = 50)
ent_city.grid(row = 4, column = 1)

# State/Province
lbl_state = tk.Label(master = frame_1, text = "State:")
lbl_state.grid(row = 5, column = 0, sticky = "e")
ent_state = tk.Entry(master = frame_1, width = 50)
ent_state.grid(row = 5, column = 1)

# Postal Code
lbl_post = tk.Label(master = frame_1, text = "Postal Code:")
lbl_post.grid(row = 6, column = 0, sticky = "e")
ent_post = tk.Entry(master = frame_1, width = 50)
ent_post.grid(row = 6, column = 1)

# Country
lbl_country = tk.Label(master = frame_1, text = "Country:")
lbl_country.grid(row = 7, column = 0, sticky = "e")
ent_country = tk.Entry(master = frame_1, width = 50)
ent_country.grid(row = 7, column = 1)

# Frame 2 - contains Clear and Submit buttons
frame_2 = tk.Frame(borderwidth = 4)
frame_2.grid(row = 1, column = 0, padx = 2, pady = 2, sticky = "e")

# Clear button
btn_clear = tk.Button(master = frame_2, text = "Clear")
btn_clear.grid(row = 0, column = 0, ipadx = 10, padx = 10)

# Submit button
btn_submit = tk.Button(master = frame_2, text = "Submit")
btn_submit.grid(row = 0, column = 1, ipadx = 10)
#------------------------

window.mainloop()
