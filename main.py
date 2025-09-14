from pyrubi import Client
from pyrubi.types import Message
from threading import Thread
import asyncio

bot = Client(session="otamsan")

group = "گوید_گپ"
ekh = 0
ekhgu = []

def delet(m):
    m.delete()

async def For(m):
    global ekhgu
    try:
        admins = bot.get_admin_members(group,just_get_guids=True)
        if m.author_guid in admins:
            print("Admin")
        else:
            Thread(target=delet,args=[m]).start()
    except Exception as e:
        print(e)

async def Text(m):
    try:
        admins = bot.get_admin_members(group,just_get_guids=True)
        if m.author_guid in admins:
            print("Admin Send Link.")
        else:
            Thread(target=delet,args=[m]).start()
    except Exception as e:print(e)
    
def run_async(coroutine):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(coroutine)
    loop.close()


@bot.on_message(filters=['Group'])
def update(m:Message):
    if m.object_guid == group:
        if m.is_forward:
            Thread(target=run_async,args=[For(m)]).start()
        elif "@" in m.text or "https" in m.text or "or" in m.text or "www" in m.text:
            Thread(target=run_async,args=[Text(m)]).start()
        elif m.has_link:
            Thread(target=run_async,args=[Text(m)]).start()
        
            
bot.run()