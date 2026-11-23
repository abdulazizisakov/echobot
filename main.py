from telegram import Bot

from settings import TOKEN


bot = Bot(TOKEN)

updates = bot.get_updates()
print(updates)
