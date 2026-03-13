
def calculate_yield(principal, monthly_earned):
    """
    Calculates monthly interest rate and extrapolates yearly rate.
    """
    # Calculate monthly rate as a decimal
    monthly_rate = monthly_earned / principal
    
    # Simple extrapolation (Annual Percentage Rate - APR)
    annual_rate = monthly_rate * 12
    
    # Compound extrapolation (Annual Percentage Yield - APY)
    # Formula: ((1 + r)^12) - 1
    apy_rate = ((1 + monthly_rate) ** 12) - 1
    
    return monthly_rate, annual_rate, apy_rate

# --- User Inputs ---
# Example: $50,000 balance, $210 earned this month
balance = 25996.95 
interest_received = 199.05

m_rate, a_rate, apy = calculate_yield(balance, interest_received)

# --- Results ---
print(f"--- Investment Summary ---")
print(f"Monthly Interest Rate: {m_rate:.4%}")
print(f"Annual Rate (Simple):  {a_rate:.2%}")
print(f"Annual Yield (APY):    {apy:.2%}")
