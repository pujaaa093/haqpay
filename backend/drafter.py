def generate_complaint_letter(worker_name: str, sector: str, area: str, days: int, 
                              hours: float, paid: float, expected: float, stolen: float) -> str:
    return f"""FORMAL GRIEVANCE REGARDING WAGE THEFT & MINIMUM WAGE VIOLATION

To,
The District Labour Officer / District Legal Services Authority (DLSA),
Bengaluru Urban District, Karnataka.

Subject: Complaint under Section 20 of the Minimum Wages Act, 1948 & Code on Wages, 2019

Respected Sir/Madam,

I am submitting this formal complaint on behalf of the affected informal sector worker detailed below:

1. WORKER DETAILS:
   - Name: {worker_name}
   - Sector: {sector}
   - Work Location/Area: {area}, Bengaluru

2. VIOLATION SUMMARY:
   - Total Days Worked: {days} days
   - Daily Working Hours: {hours} hours/day
   - Total Amount Received: ₹{paid:.2f}
   - Statutory Minimum Entitlement: ₹{expected:.2f}
   - TOTAL STOLEN WAGES DEMANDED: ₹{stolen:.2f}

3. LEGAL GROUNDS:
   - Failure to pay statutory minimum rates under Karnataka Labour Department Notification.
   - Non-payment of Overtime Wages at double the standard rate for hours worked beyond 8 hours daily.

We request immediate intervention to cause an inquiry, recover unpaid wages along with statutory compensation, and take penal action against the employer.

Date: 28/10/2026
Submitted via: HaqPay Legal Grievance System
"""