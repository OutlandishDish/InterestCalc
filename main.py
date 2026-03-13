import tkinter as tk
from tkinter import messagebox
from calculations import calculate_yield 

def update_current_balance(*args):
    """Calculates: Current Balance = Original Balance - Interest Earned"""
    try:
        # Get values or default to 0 if empty
        orig_val = var_original.get()
        earned_val = var_interest.get() # This is the shared variable
        
        orig = float(orig_val) if orig_val else 0
        earned = float(earned_val) if earned_val else 0
        
        current = orig - earned
        var_current.set(f"{current:.2f}")
    except ValueError:
        pass 

def run_calculation(event=None):
    try:
        p = float(var_current.get())
        m = float(var_interest.get())
        d = float(entry_days.get())
        
        m_rate, a_rate, apy = calculate_yield(p, m, d)
        
        lbl_res.config(text=f"Standard Monthly: {m_rate:.4%}\n"
                            f"Annual Yield (APY): {apy:.2%}")
    except ValueError:
        messagebox.showerror("Input Error", "Please ensure all fields have numbers.")

root = tk.Tk()
root.title("Savings Mirror Tracker")
root.geometry("380x480")

# --- Variables ---
var_original = tk.StringVar()
var_interest = tk.StringVar() # This is the KEY - one variable for two fields
var_current = tk.StringVar()

var_original.trace_add("write", update_current_balance)
var_interest.trace_add("write", update_current_balance)

# --- UI Layout ---

# 1. Original Balance
tk.Label(root, text="Step 1: Original Balance ($):", font=("Arial", 10, "bold")).pack(pady=5)
entry_orig = tk.Entry(root, textvariable=var_original)
entry_orig.pack()

# 2. Interest Earned (THE INPUT)
tk.Label(root, text="Step 2: Enter Interest Earned ($):", font=("Arial", 10, "bold")).pack(pady=5)
entry_interest_input = tk.Entry(root, textvariable=var_interest)
entry_interest_input.pack()

# 3. Mirror Field (THE DISPLAY)
# By using state='readonly', you can't click in here, but it mirrors Step 2
tk.Label(root, text="Mirrored Interest (Read Only):").pack(pady=5)
tk.Entry(root, textvariable=var_interest, state='readonly', fg="blue").pack()

# 4. Resulting Principal
tk.Label(root, text="Current Principal (calculated):").pack(pady=5)
tk.Entry(root, textvariable=var_current, state='readonly', font=("Arial", 10, "bold")).pack()

# 5. Days
tk.Label(root, text="Days in Period:").pack(pady=5)
entry_days = tk.Entry(root)
entry_days.insert(0, "30")
entry_days.pack()

root.bind('<Return>', run_calculation)
tk.Button(root, text="Calculate APY", command=run_calculation, bg="#4CAF50", fg="white").pack(pady=20)

lbl_res = tk.Label(root, text="Press Enter to calculate", font=("Arial", 10, "italic"))
lbl_res.pack()

# Set initial focus to the top field
entry_orig.focus_set()

root.mainloop()