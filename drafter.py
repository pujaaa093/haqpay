def generate_complaint_letter(worker_name: str, sector: str, area: str, days_worked: int, hours_per_day: float, amount_paid: float, expected_pay: float, wage_stolen: float):
    letter = f"""
FORMAL COMPLAINT REGARDING NON-PAYMENT OF MINIMUM WAGES

To,
The Labour Officer,
{area}

Applicant: {worker_name}
Sector: {sector}

Respected Sir/Madam,

I am writing to lodge a formal complaint regarding wage underpayment. 

Details of Work:
- Days Worked: {days_worked}
- Average Hours per Day: {hours_per_day}
- Amount Paid: ₹{amount_paid:.2f}
- Prescribed Minimum Pay: ₹{expected_pay:.2f}
- Total Stolen/Shortfall Wages: ₹{wage_stolen:.2f}

I request your immediate intervention to recover the shortfall of ₹{wage_stolen:.2f} as per the Minimum Wages Act.

Sincerely,
{worker_name}
    """.strip()
    return letter