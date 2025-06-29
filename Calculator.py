import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Function to handle button click
def on_button_click(char):
    current_text = entry.get()
    new_text = current_text + str(char)
    entry.delete(0, tk.END)
    entry.insert(tk.END, new_text)

# Function to clear the entry
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget for the display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid')
entry.grid(row=0, column=0, columnspan=4)

# Define button labels
button_labels = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create and place buttons in the grid
row = 1
col = 0
for label in button_labels:
    if label == 'C':
        button = tk.Button(root, text=label, width=5, height=2, font=('Arial', 18), command=clear_entry)
    elif label == '=':
        button = tk.Button(root, text=label, width=5, height=2, font=('Arial', 18), command=lambda: evaluate_expression(entry.get()))
    else:
        button = tk.Button(root, text=label, width=5, height=2, font=('Arial', 18), command=lambda char=label: on_button_click(char))
    
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()