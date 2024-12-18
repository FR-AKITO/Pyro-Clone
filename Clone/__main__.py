import pyrogram 

# Set up bot configurations
API_ID = 25629197
API_HASH = "fd41f8bacda97ab0a3ad120b30339978"
TOKEN = "7402282033:AAEv5Aq37Kf6vCj8k1GVnCEcnuDCIXWvHMk"

#PYROGRAM BOT CLIENT
bot = Client(name="CloneBot", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=dict(root="Clone.Examples"))

if __name__ == "__main__":
      bot.run()
