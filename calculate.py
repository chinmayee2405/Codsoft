import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
        else:
            messagebox.showerror("Error", "Please select an operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Input fields
tk.Label(root, text="Enter First Number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter Second Number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Operation selection
tk.Label(root, text="Choose Operation:").pack(pady=5)
operation_var = tk.StringVar(value="None")
operations = ["Addition", "Subtraction", "Multiplication", "Division"]
for op in operations:
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).pack(anchor="w")


# Calculate button
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

# Run the GUI
root.mainloop()
