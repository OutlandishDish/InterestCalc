# calculations.py

def calculate_yield(principal, monthly_earned, days):
    if principal <= 0 or days <= 0:
        return 0, 0, 0
    
    # Calculate the rate earned per day
    daily_rate = (monthly_earned / principal) / days
    
    # Simple Annual Rate (APR) based on 365 days
    annual_rate = daily_rate * 365
    
    # Annual Yield (APY) assuming daily compounding
    apy_rate = (1 + daily_rate)**365 - 1
    
    # For display, we can still show a 30-day "standard" monthly rate
    monthly_display_rate = daily_rate * 30
    
    return monthly_display_rate, annual_rate, apy_rate