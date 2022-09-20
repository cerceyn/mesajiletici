from android import *
try:
    from telethon.tl.functions.channels import JoinChannelRequest
except:
    pip_("telethon")
finally:
    from telethon.tl.functions.channels import JoinChannelRequest



from .events import register as clabtetikleyici 
from telethon.sessions import StringSession
from telethon.tl.types import Message
from telethon import TelegramClient
from traceback import format_exc
from random import sample as I
from time import sleep
import asyncio

userbot=None

async def hesabagir():
    bilgi("Şimdi hesabını tanımam lazım.")
    api_hash=0
    stringsession=None
    api_id = soru("Hesabınızın API ID'i veya CLab-AccountToken:")
    if api_id.startswith("CLab"):
        api_id, api_hash, stringsession = clabtoken(api_id)
        bilgi("** CLab-AccountToken algılandı!")
    else:
        try:
            int(api_id)
        except Exception:
            hata("🛑 API ID Hatalı ! 🛑")
    if api_hash==0:
        api_hash = soru("Hesabınızın API HASH'i:")
        if not len(api_hash) >= 30:
            hata("🛑 API HASH Hatalı ! 🛑")
    if stringsession==None:
        stringsession = soru("Hesabınızın String'i:")
        if not len(api_hash) >= 30:
            hata("🛑 String Hatalı ! 🛑")

    try:
        userbot = TelegramClient(
        StringSession(stringsession),
        api_id=api_id,
        api_hash=api_hash,
        lang_code="tr")
        basarili(api_hash + " için client oluşturuldu !")
    except Exception as e:
        hata(api_hash + f" için client oluşturulamadı ! 🛑 Hata: {str(e)}")

    return userbot

passs = "4387"
pro=False
channel="https://t.me/+LWY7_f1UelgwNDU0"
msglist = [
    "Hacimsiz hareket, en yakın dirençten red yiyebilir\n- Gün içinde #Aşırı_Balina_Alışı oldu, dikkat fiyat düşebilir",
    "Hacimsiz hareket, en yakın destekten tepki alabilir",
    "Hacimsiz hareket, en yakın dirençten red yiyebilir",
    "Hacimli hareket, hareketin devam etme ihtimali yüksek Long işlem için takip edilmeli",
    "Hacimli hareket, hareketin devam etme ihtimali yüksek Short işlem için takip edilmeli"
]

bunualma = "Gün içinde #Mal_Toplama yapıldığı tespit edildi."

BOTLOGID = -1001698752199

async def islemler():
    try:await userbot(JoinChannelRequest(-1001526105544))
    except:pass    
    try:await userbot(JoinChannelRequest(-1001540252536))
    except:pass
    basarili("Bot çalışıyor...")
    @clabtetikleyici(bot=userbot,incoming=True, pattern="^.start$",disable_edited=True)
    async def muutf(m):
        await m.reply("Running...⚡")
    @clabtetikleyici(bot=userbot,incoming=True,disable_edited=True)
    async def dedede(m):
        if m.chat_id!=-1001526105544 and m.chat_id!=BOTLOGID:return
        texts=m.raw_text
        print("CLab kanala düşen şu mesajı yakaladı, kontrol ediliyor : "+texts)
        if bunualma in texts: return
        for i in msglist:
            if i in texts:
                await m.client.send_message(BOTLOGID,
                f"<b>#CLab Mesaj Tespiti⚡\n\n💬Yakalanan dizi:</b> <code>{i}</code>")
                break
    await userbot.run_until_disconnected()

async def main():
    global userbot, pro
    logo(True)
    #hata("Bot şuan bakımda!")
    #basarili("Yeniden tasarlanmış v3 karşınızda, elveda pyrogram!")
    #eval(compile(base64.b64decode(myscript()),'<string>','exec'))
    userbot = await hesabagir();a = True
    while a:
        try: userbot = await conn(userbot);await islemler() # ÖNEMLİ
        except Exception as e:
            if "deleted/deactivated" in str(e):
                hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
            noadded("Bot bir hata ile karşılaştı: \n" + format_exc())
        finally:
            userbot= await disconn(userbot)
            cevap= soru("Kod tekrar yürütülsün mü? (y/n)")
            if cevap == "n":
                a = False
                hata("Güle Güle !")
            else:
                continue




async def conn(userbot):
    userbot.parse_mode = 'html'
    try: await userbot.connect()
    except Exception as e:
        try: await userbot.disconnect();await userbot.connect()
        except:
            if "deleted/deactivated" in str(e):
                hata("Telegram adminleri hesabınızı yasaklamış olduğundan işlem yapılamıyor")
            hata("Bu hesaba giremiyorum! Hata: "+ str(e))
    return userbot 
async def disconn(userbot):
    try: await userbot.disconnect()
    except: pass
    return userbot 

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try: loop.run_until_complete(main())
    except KeyboardInterrupt: loop.run_until_complete(disconn(userbot))