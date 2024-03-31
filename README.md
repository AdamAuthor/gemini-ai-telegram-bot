# 🤖 Gemini AI Telegram Bot

This is a Telegram bot integrated with Google's Gemini AI. It uses the Gemini AI to generate responses to user messages.

## 🌟 Features

- Responds to user messages using Google's Gemini AI.
- Handles all types of user messages.
- Deletes the "Please wait..." message after the response is generated.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher
- pip
- A Telegram Bot API key
- A Google API key

### Installing

1. Clone the repository:
```bash
git clone https://github.com/AdamAuthor/gemini-ai-telegram-bot
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory of the project and add the following environment variables:
```env
TELEGRAM_BOT_API_KEY=YOUR_TELEGRAM_BOT_API_KEY
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

4. Run the bot:
```bash
python presentation_layer.py
```

## 🎮 Usage

1. Start a chat with the bot on Telegram.
2. Send a message to the bot.
3. The bot will respond with a "Please wait..." message.
4. The bot will generate a response using the Gemini AI and send it to you.