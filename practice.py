import tkinter as tk
from tkinter import messagebox
import sympy as sp


def simplify_expression():
    expr = expression_entry.get()
    try:
        expression = sp.sympify(expr)
        simplified = sp.simplify(expression)
        result_label.config(text=f"Simplified: {simplified}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def expand_expression():
    expr = expression_entry.get()
    try:
        expression = sp.sympify(expr)
        expanded = sp.expand(expression)
        result_label.config(text=f"Expanded: {expanded}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def solve_equation():
    expr = expression_entry.get()
    var = variable_entry.get()
    try:
        variable = sp.symbols(var)
        equation = sp.Eq(sp.sympify(expr), 0)
        solutions = sp.solve(equation, variable)
        result_label.config(text=f"Solutions: {solutions}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def differentiate_expression():
    expr = expression_entry.get()
    var = variable_entry.get()
    try:
        variable = sp.symbols(var)
        expression = sp.sympify(expr)
        derivative = sp.diff(expression, variable)
        result_label.config(text=f"Derivative: {derivative}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def integrate_expression():
    expr = expression_entry.get()
    var = variable_entry.get()
    try:
        variable = sp.symbols(var)
        expression = sp.sympify(expr)
        integral = sp.integrate(expression, variable)
        result_label.config(text=f"Integral: {integral}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("SymPy Practice")

# Create and place the expression label and entry
expression_label = tk.Label(root, text="Expression:")
expression_label.pack()
expression_entry = tk.Entry(root, width=50)
expression_entry.pack()

# Create and place the variable label and entry
variable_label = tk.Label(root, text="Variable (for differentiation/integration/solving):")
variable_label.pack()
variable_entry = tk.Entry(root, width=50)
variable_entry.pack()

# Create and place the buttons
simplify_button = tk.Button(root, text="Simplify", command=simplify_expression)
simplify_button.pack()
expand_button = tk.Button(root, text="Expand", command=expand_expression)
expand_button.pack()
solve_button = tk.Button(root, text="Solve Equation", command=solve_equation)
solve_button.pack()
differentiate_button = tk.Button(root, text="Differentiate", command=differentiate_expression)
differentiate_button.pack()
integrate_button = tk.Button(root, text="Integrate", command=integrate_expression)
integrate_button.pack()

# Create and place the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()
