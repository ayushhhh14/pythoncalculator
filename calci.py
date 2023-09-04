import tkinter as tk
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "+":
      result.set(num1 + num2)

    elif operation == "-":
     result.set(num1 - num2)
    elif operation == "*":

        result.set(num1 * num2)
    elif operation == "/":
       if num2 != 0:
            result.set(num1 / num2)

    else:
      result.set("Cannot divide by zero")

root = tk.Tk()

root.title("Simple Calculator")

root.configure(bg="#f0f0f0")  # Light gray

entry_num1 = tk.Entry(root, bg="white")

entry_num1.pack()

entry_num2 = tk.Entry(root, bg="white")

entry_num2.pack()
operation_var = tk.StringVar()

operation_var.set("+")

operations = ["+", "-", "*", "/"]

for op in operations:

  tk.Radiobutton(root, text=op, variable=operation_var, value=op, bg="#f0f0f0").pack()

 # adding calculate button
  calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="green", fg="white")
  calculate_button.pack()
# adding result label

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, bg="#f0f0f0", fg="blue")
result_label.pack()
root.mainloop()