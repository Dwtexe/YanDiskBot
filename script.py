import sys
import os
import yadisk
import sys
import time
import logging

# Import the client
from telethon import TelegramClient, events
from telethon import events
from telethon.tl.custom import Button

# Define some variables so the code reads easier
session = "tg_downloader"
api_id = 6
api_hash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
bot_token = "950406168:AAE78QgfgwZlKgiLZs5JH2ZAjpNCBRlNz1Y"
download_path = "/root/antinude/nude.jpg" # Full path
debug_enabled = "true"
user_id = "452321614"
group_id = "-1001242475700"
proxy = None  # https://github.com/Anorov/PySocks

client = TelegramClient(session, api_id, api_hash, proxy=proxy)
logging.basicConfig(level=logging.WARNING)

# This is our update handler. It is called when a new update arrives.
# Register `events.NewMessage` before defining the client.
@client.on(events.CallbackQuery)
async def callback(event):
    if format(event.data) == "b'sil'":
        await event.edit("veri")
    if format(event.data) == "b'mute'":
        await event.edit("veri")
    if format(event.data) == "b'ban'":
        await event.edit("veri")
@events.register(events.NewMessage)
async def handler(update):
    if update.message.media is not None:
        userid = update.message.from_id
        print(update.message)
        if os.path.isfile(str(userid)):
            tokenfile = open(str(userid),'r')
            token2 = tokenfile.read()
            download_result = await client.download_media(update.message, download_path)
            y = yadisk.YaDisk(token=token2)
            y.upload("yusuf.txt", "yusuf3.txt")
            y.publish("yusuf3.txt");
            link = y.get_meta("yusuf2.txt").public_url
            await update.reply(link)
        else:
            y = yadisk.YaDisk("7ab5436b2b83434390f569d5f92c9b69", "167dfabacd3a4fa9b749cd4b1af42758")
            url = y.get_code_url()
            async with client.conversation(userid) as conv:
                await conv.send_message("Aşağıdaki butona tıklayıp yandexin websitesine gideceksiniz, ardından uygulamaya izin veriniz, izin verdikten sonra bir kod alacaksınız. O kodu yazınız.", buttons=[
    [
    [Button.url('Bu uygulamaya izin ver', url)]])
                code = await conv.get_response()
                response = y.get_token(code.raw_text)
                y.token = response.access_token

            if y.check_token():
                await update.reply("Token başarılı bir şekilde kaydedildi!")
                dosya = open(str(userid),"w",encoding="utf-8")
                dosya.write(y.token)
            else:
                await update.reply("Something went wrong. Not sure how though...")
        

    elif update.message.message == "/start":
       await update.reply('Hello! I am antinude bot!') 
    elif update.message.message == "/settings":
       await update.reply('This command is developing!:', buttons=[ [Button.inline('mute')], [Button.inline('Left')], [Button.inline('Left')]]) 

try:
    # Start client with TG_BOT_TOKEN string
    client.start(bot_token=str(bot_token))
    # Register the update handler so that it gets called
    client.add_event_handler(handler)

    # Run the client until Ctrl+C is pressed, or the client disconnects
    print('Successfully started (Press Ctrl+C to stop)')
    client.run_until_disconnected()
finally:
    client.disconnect()
    print('Stopped!')
