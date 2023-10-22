from telegram.ext import *
import requests
import asyncio
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
async def start_commmand(update):
    print('I am here')
    await update.message.reply_text('Hello! Welcome To Store!')
def main():
    application = Application.builder().token(
        "6387075484:AAE17jGNwdMEJb1ozhZXMV2-Uo9FqOcxGZg").build()
    # Commands
    application.add_handler(CommandHandler(
        'start', CommandHandler('start_commmand', start_commmand)))
    # Run bot
    application.run_polling(1.0)
if __name__ == '__main__':
    main()