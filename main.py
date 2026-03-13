import tkinter as tk
from tkinter import messagebox
from calculations import calculate_yield 

def run_calculation(event=None):
    try:
        p = float(entry_balance.get())
        m = float(entry_interest.get())
        d = float(entry_days.get()) # Get the days
        
        m_rate, a_rate, apy = calculate_yield(p, m, d)
        
        lbl_res.config(text=f"Standard Monthly: {m_rate:.4%}\n"
                            f"Annual (Simple): {a_rate:.2%}\n"
                            f"Annual Yield (APY): {apy:.2%}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Precision Interest Calculator")
root.geometry("350x300")

# Balance Input
tk.Label(root, text="Current Balance ($):").pack()
entry_balance = tk.Entry(root)
entry_balance.pack(pady=5)

# Interest Input
tk.Label(root, text="Interest Earned ($):").pack()
entry_interest = tk.Entry(root)
entry_interest.pack(pady=5)

# Days Input
tk.Label(root, text="Days in this period (e.g., 28 or 31):").pack()
entry_days = tk.Entry(root)
entry_days.insert(0, "30") # Set 30 as a default starting value
entry_days.pack(pady=5)

root.bind('<Return>', run_calculation)  # Bind Enter key to calculation
tk.Button(root, text="Calculate", command=run_calculation, bg="#2196F3", fg="white").pack(pady=15)

lbl_res = tk.Label(root, text="Enter details and click Calculate", font=("Arial", 10))
lbl_res.pack()

root.mainloop()