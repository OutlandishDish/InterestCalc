# TODO: Change icon.
# Review Code for understanding
# Creat back end to store data, lookiat incorporating it into my budgeting solution.

import tkinter as tk
from tkinter import messagebox
from calculations import calculate_yield 

def update_principal(*args):
    """Calculates: Base Principal = Current Balance - Interest Earned"""
    try:
        # Get values from the variables
        curr_bal = var_balance.get()
        earned_val = var_interest.get()
        
        # Convert to float, defaulting to 0 if empty
        bal = float(curr_bal) if curr_bal else 0
        earned = float(earned_val) if earned_val else 0
        
        # Base principal is the money you started the month with
        principal = bal - earned
        var_principal.set(f"{principal:.2f}")
    except ValueError:
        pass 

def run_calculation(event=None):
    try:
        # We calculate yield based on the 'Base Principal' 
        p = float(var_principal.get())
        m = float(var_interest.get())
        d = float(entry_days.get())
        
        m_rate, a_rate, apy = calculate_yield(p, m, d)
        
        lbl_res.config(text=f"Standard Monthly: {m_rate:.4%}\n"
                            f"Annual Yield (APY): {apy:.2%}", fg="black")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Savings Interest v3.1")
root.geometry("350x420")

# --- Variables & Tracing ---
var_balance = tk.StringVar()
var_interest = tk.StringVar()
var_principal = tk.StringVar()

var_balance.trace_add("write", update_principal)
var_interest.trace_add("write", update_principal)

# --- UI ---
# Field 1: Current Balance
tk.Label(root, text="Current Balance ($):", font=("Arial", 10, "bold")).pack(pady=5)
entry_bal = tk.Entry(root, textvariable=var_balance)
entry_bal.pack()

# Field 2: Interest Earned
tk.Label(root, text="Interest Earned ($):", font=("Arial", 10, "bold")).pack(pady=5)
tk.Entry(root, textvariable=var_interest).pack()

# Field 3: Base Principal (Calculated)
tk.Label(root, text="Base Principal (Calculated):").pack(pady=5)
tk.Entry(root, textvariable=var_principal, state='readonly', fg="green").pack()

# Field 4: Days
tk.Label(root, text="Days in Period:").pack(pady=5)
entry_days = tk.Entry(root)
entry_days.insert(0, "30")
entry_days.pack()

root.bind('<Return>', run_calculation)
tk.Button(root, text="Calculate", command=run_calculation, bg="#2196F3", fg="white").pack(pady=20)

lbl_res = tk.Label(root, text="Press Enter to calculate yield", font=("Arial", 10, "italic"))
lbl_res.pack()

entry_bal.focus_set()
root.mainloop()