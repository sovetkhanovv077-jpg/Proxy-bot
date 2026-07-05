from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8621111465:AAGC-9cBg5zvQhAioU4aZYAL-z6BApQXyRE"

keyboard = [
    ["🛒 Товары"],
    ["👤 Профиль"]
]

reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Добро пожаловать!",
        reply_markup=reply_markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛒 Товары":
        await update.message.reply_text(
            "📂 Категория: FF iOS\n\n"
            "🟢 Proxy 1 Day | $2\n"
            "🟢 Proxy 7 Day | $5\n"
            "🟢 Proxy 31 Day | $10"
        )

    elif text == "👤 Профиль":
        await update.message.reply_text(
            f"👤 Ваш ID: {update.effective_user.id}\n"
            f"👋 Логин: @{update.effective_user.username}"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, buttons))

app.run_polling()
