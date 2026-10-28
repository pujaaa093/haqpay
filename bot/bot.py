import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BACKEND_API_URL = "http://localhost:8000/complaints"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to HaqPay / ಹಕ್ ಪೇ / हकपे!\n\n"
        "Please send a text or voice message detailing your work, hours, location, and amount paid."
    )

async def handle_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice_file = await context.bot.get_file(update.message.voice.file_id)
    file_path = "temp_voice.ogg"
    await voice_file.download_to_drive(file_path)

    # Process audio
    from voice import transcribe_audio, extract_fields
    transcript = transcribe_audio(file_path)
    data = extract_fields(transcript)

    # Push to Backend API
    response = requests.post(BACKEND_API_URL, json=data)
    if response.status_code == 200:
        res = response.json()
        await update.message.reply_text(
            f"✅ Complaint Registered!\n\n"
            f"Expected Wage: ₹{res['expected_pay']}\n"
            f"Paid: ₹{res['amount_paid']}\n"
            f"Stolen Amount: ₹{res['wage_stolen']}\n\n"
            f"Your complaint has been forwarded to the Labour Department."
        )
    else:
        await update.message.reply_text("Error submitting complaint. Please try again.")

if __name__ == "__main__":
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice))
    app.run_polling()