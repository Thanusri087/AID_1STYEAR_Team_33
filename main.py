import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert_weight():
    try:
        choice_str = choice_var.get()
        choice = int(choice_str.split('.')[0])

        value = float(entry_value.get())

        if choice == 1:
            result = value * 1000
            output = f"{value} kilograms = {result} grams"
        elif choice == 2:
            result = value / 1000
            output = f"{value} grams = {result} kilograms"
        elif choice == 3:
            result = value * 2.20462
            output = f"{value} kilograms = {result} pounds"
        elif choice == 4:
            result = value / 2.20462
            output = f"{value} pounds = {result} kilograms"
        elif choice == 5:
            result = value / 453.592
            output = f"{value} grams = {result} pounds"
        elif choice == 6:
            result = value * 453.592
            output = f"{value} pounds = {result} grams"
        else:
            output = "Invalid choice! Please enter a number between 1 and 6."

        label_result.config(text=output)
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numeric values.")

root = tk.Tk()
root.title("Weight Unit Converter")

choices = [
    "1. Kilograms to grams",
    "2. Grams to kilograms",
    "3. Kilograms to pounds",
    "4. Pounds to kilograms",
    "5. Grams to pounds",
    "6. Pounds to grams"
]

choice_var = tk.StringVar(value=choices[0])
ttk.Label(root, text="Select conversion type:").pack(pady=5)
dropdown = ttk.Combobox(root, values=choices, textvariable=choice_var, state="readonly")
dropdown.pack(pady=5)

ttk.Label(root, text="Enter the weight value:").pack(pady=5)
entry_value = ttk.Entry(root)
entry_value.pack(pady=5)

btn_convert = ttk.Button(root, text="Convert", command=convert_weight)
btn_convert.pack(pady=10)

label_result = ttk.Label(root, text="", font=('Arial', 12, 'bold'))
label_result.pack(pady=10)

root.mainloop()
