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

# Create the main frame
master_frame = ttk.Frame(master=window, padding=padd)
master_frame.pack()

# Create frames and buttons in a grid
for row in range(len(ranks)):
    for col in range(len(suits)):
        # Create a container frame for each cell
        cell_frame = ttk.Frame(
            master=master_frame,
            width=cell_width,
            height=cell_height
        )
        cell_frame.grid(row=row, column=col, padx=2, pady=2)
        cell_frame.pack_propagate(False)
        
        # Create button inside the cell frame
        button = tk.Button(
            master=cell_frame,  # Important: button goes inside cell_frame
            text=f'{ranks[row]}{suits[col]}',
            bg="#7BB274",
            fg="white",
            font=("Arial", 12),
            command=lambda btn=None: None
        )
        button.configure(command=lambda b=button: change_colour(b))
        button.pack(fill=tk.BOTH, expand=True)  # Fill the cell frame

window_width = 2 * padd + len(suits) * (cell_width + 4)  # +4 for grid padding
window_height = 2 * padd + len(ranks) * (cell_height + 4)

window.geometry(f"{window_width}x{window_height}")
window.resizable(False, False)

window.mainloop()