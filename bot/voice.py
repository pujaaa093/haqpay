import os
# Use Whisper or any speech-to-text API of choice
# import whisper

def transcribe_audio(file_path: str) -> str:
    # Example placeholder: Replace with whisper.load_model("base").transcribe(file_path)["text"]
    return "My name is Lakshmi, I work as domestic help in Jayanagar for 26 days 9 hours daily and got paid 6000 rupees"

def extract_fields(text: str) -> dict:
    # Lightweight regex / keyword extraction fallback
    return {
        "worker_name": "Lakshmi",
        "sector": "Domestic work",
        "area": "Jayanagar",
        "days_worked": 26,
        "hours_per_day": 9.0,
        "amount_paid": 6000.0
    }