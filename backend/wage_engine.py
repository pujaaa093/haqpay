# Standard daily rates based on Karnataka Labour Dept (Zone 1 / BBMP)
RATES_PER_DAY = {
    "Domestic work": 899.09,    # Unskilled
    "Construction": 989.00,     # Semi-Skilled
    "Security": 1087.90,        # Skilled
    "Driver": 1087.90,          # Skilled
    "Cleaning": 899.09,         # Unskilled
    "Factory / General": 899.09 # Unskilled
}

STANDARD_HOURS = 8.0

def calculate_stolen_wages(sector: str, days_worked: int, hours_per_day: float, amount_paid: float) -> dict:
    daily_rate = RATES_PER_DAY.get(sector, 899.09)
    hourly_rate = daily_rate / STANDARD_HOURS
    
    # Overtime calculation: Hours worked beyond 8 hrs/day are paid at 2x rate
    overtime_hours = max(0.0, hours_per_day - STANDARD_HOURS)
    regular_hours = min(hours_per_day, STANDARD_HOURS)
    
    daily_expected = (regular_hours * hourly_rate) + (overtime_hours * hourly_rate * 2.0)
    total_expected = daily_expected * days_worked
    wage_stolen = max(0.0, total_expected - amount_paid)
    
    is_violation = wage_stolen > 50  # Allow minor rounding threshold
    
    return {
        "expected_pay": round(total_expected, 2),
        "actual_pay": amount_paid,
        "wage_stolen": round(wage_stolen, 2),
        "overtime_hours_per_day": overtime_hours,
        "is_violation": is_violation
    }