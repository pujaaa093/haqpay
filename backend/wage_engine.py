def calculate_stolen_wages(sector: str, days_worked: int, hours_per_day: float, amount_paid: float):
    # Base daily rates (to be dynamically linked with legal research data)
    sector_rates = {
        "plantation": 450.0,
        "security": 600.0,
        "construction": 650.0
    }
    
    daily_rate = sector_rates.get(sector.lower(), 500.0)
    expected_pay = daily_rate * days_worked
    wage_stolen = max(0.0, expected_pay - amount_paid)
    
    return {
        "daily_rate": daily_rate,
        "expected_pay": expected_pay,
        "wage_stolen": wage_stolen
    }