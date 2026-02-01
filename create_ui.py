import tkinter as tk
from tkinter import ttk 

cell_width = 50
cell_height = 50
padd = 10

suits = ['♣', '♦', '♥', '♠']
ranks = ['A', 'K', 'Q', 'J', '10']

def change_colour(button):
    current_bg = button.cget("bg")
    if current_bg == "#7BB274":
        button.configure(bg="#D3494E", fg="white")
    else:
        button.configure(bg="#7BB274", fg="white")

window = tk.Tk()
window.title('Card counter')
window.resizable(False, False)

# creating the frames of all suits and rank in the form of a matrix

master_frame = ttk.Frame(master = window, padding = padd)
master_frame.pack()

for row in range(len(ranks)):
    for col in range(len(suits)):
        frame = ttk.Frame(
            master = master_frame,
            borderwidth = 1,
            width = cell_width,
            height = cell_height
        )
        frame.grid(row = row, column = col, padx = 2, pady = 2)
        frame.pack_propagate(False)

        button = tk.Button(
            master=master_frame,
            text=f'{ranks[row]}{suits[col]}',
            bg="#7BB274",
            fg="white",
            font=("Arial", 12),
            width=6,
            height=3,
            command=lambda r=row, c=col, btn=None: None
        )
        button.configure(command=lambda b=button: change_colour(b))
        button.grid(row=row, column=col, padx=2, pady=2)


window_width  = 2 * padd + len(suits) * (cell_width  + 18)
window_height = 2 * padd + len(ranks) * (cell_height + 22)

window.geometry(f"{window_width}x{window_height}")

window.mainloop()