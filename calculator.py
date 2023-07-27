import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        choice = operation_choice.get()

        if choice == 1:
            result = add(num1, num2)
        elif choice == 2:
            result = subtract(num1, num2)
        elif choice == 3:
            result = multiply(num1, num2)
        elif choice == 4:
            result = divide(num1, num2)
        else:
            result = "Invalid choice. Please select a valid operation."

        label_result.config(text="Result: " + str(result))

    except ValueError:
        label_result.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create widgets
label_num1 = tk.Label(root, text="Enter the first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter the second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

operation_choice = tk.IntVar()
operation_choice.set(1)

operations_frame = tk.Frame(root)
operations_frame.pack()

radio_add = tk.Radiobutton(operations_frame, text="Addition", variable=operation_choice, value=1)
radio_add.pack(side=tk.LEFT)

radio_subtract = tk.Radiobutton(operations_frame, text="Subtraction", variable=operation_choice, value=2)
radio_subtract.pack(side=tk.LEFT)

radio_multiply = tk.Radiobutton(operations_frame, text="Multiplication", variable=operation_choice, value=3)
radio_multiply.pack(side=tk.LEFT)

radio_divide = tk.Radiobutton(operations_frame, text="Division", variable=operation_choice, value=4)
radio_divide.pack(side=tk.LEFT)

btn_calculate = tk.Button(root, text="Calculate", command=calculate)
btn_calculate.pack()

label_result = tk.Label(root, text="")
label_result.pack()

# Run the main loop
root.mainloop()
