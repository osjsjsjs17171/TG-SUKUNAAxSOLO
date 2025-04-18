import os
import logging
import telebot
import random

# Initialize your bot with the token
bot = telebot token ("7292476162:AAF2aD3F7S-_trpQqmXssxkxF44navY9--I")

emojis = ["👍", "❤", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🎉", "🤩", "🙏", 
          "👌", "😍", "❤‍🔥", "🌚", "💯", "🤣", "💔", "😐", "🇮🇳", "😈", "😴", 
          "😭", "🤓", "😇", "🤝", "🤗", "🫡", "🤪", "🗿", "🆒", "💘", "😘", 
          "😎", "🇳🇵"]

@bot.message_handler(func=lambda message: True)
def react_to_message(message):
    try:
        chat_id = message.chat.id
        message_id = message.message_id
        random_emoji = random.choice(emojis)
        
        bot.set_message_reaction(
            chat_id=chat_id,
            message_id=message_id,
            reaction=[telebot.types.ReactionTypeEmoji(random_emoji)],
            is_big=True
        )
    except Exception as e:
        print(f"Error setting reaction: {e}")
print("Bot is running...")
# Start the bot
bot.polling()

