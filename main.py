from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from wage_engine import calculate_stolen_wages
from drafter import generate_complaint_letter

app = FastAPI(title="HaqPay API Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ComplaintRequest(BaseModel):
    worker_name: str
    sector: str
    area: str
    days_worked: int
    hours_per_day: float
    amount_paid: float

# Standard JSON response (for databases/APIs)
@app.post("/complaints")
def create_complaint(data: ComplaintRequest):
    wage_summary = calculate_stolen_wages(
        data.sector, data.days_worked, data.hours_per_day, data.amount_paid
    )
    
    complaint_letter = generate_complaint_letter(
        data.worker_name, data.sector, data.area, data.days_worked,
        data.hours_per_day, data.amount_paid, 
        wage_summary["expected_pay"], wage_summary["wage_stolen"]
    )
    
    return {
        **data.model_dump(),
        **wage_summary,
        "complaint_letter": complaint_letter,
        "status": "Submitted"
    }

# HTML response (for direct human viewing in browser)
@app.post("/complaints/html", response_class=HTMLResponse)
def create_complaint_html(data: ComplaintRequest):
    record = create_complaint(data)
    letter_text = record["complaint_letter"]
    
    formatted_html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Complaint Letter - {data.worker_name}</title>
            <style>
                body {{ font-family: Arial, sans-serif; padding: 40px; background-color: #f4f4f9; }}
                .letter-box {{ background: white; padding: 40px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); max-width: 650px; margin: auto; white-space: pre-wrap; font-size: 15px; line-height: 1.6; color: #333; }}
            </style>
        </head>
        <body>
            <div class="letter-box">{letter_text}</div>
        </body>
    </html>
    """
    return formatted_html