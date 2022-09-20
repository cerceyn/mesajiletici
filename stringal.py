from android import basarili, noadded, pip_, bilgi, logo, hata, soru
import asyncio,random   

from telethon import TelegramClient
from telethon.errors import PhoneNumberInvalidError
from telethon.network import ConnectionTcpAbridged
from telethon.sessions import StringSession

loop = asyncio.get_event_loop()

class InteractiveTelegramClient(TelegramClient):
    def __init__(self, session_user_id, api_id, api_hash,
                 telefon=None, proxy=None):
        super().__init__(
            session_user_id, api_id, api_hash,
            connection=ConnectionTcpAbridged,
            proxy=proxy
        )
        self.found_media = {}
        bilgi('[i] Telegramın Sunucularına Bağlanılıyor...')
        try:
            loop.run_until_complete(self.connect())
        except IOError:
            noadded('[!] Bağlanılırken bir hata oluştu. Yeniden deneniyor...')
            loop.run_until_complete(self.connect())

        if not loop.run_until_complete(self.is_user_authorized()):
            if telefon == None:
               telefon = input('[?] Telefon Numaranız (Örnek: +90xxxxxxxxxx): ')
            user_phone = telefon
            try:
                loop.run_until_complete(self.sign_in(user_phone))
                basarili("[+] Giriş kodu gönderildi!")
            except PhoneNumberInvalidError:
                noadded(f"[-] Geçersiz Bir Numara : {user_phone}")
                return
            except ValueError:
                noadded(f"[-] Geçersiz Bir Numara : {user_phone}")
                return
            except Exception as e:
                noadded(f"[-] Şu numaraya, {user_phone} şu hatadan dolayı işlem yapılamadı: {str(e)}")
                return

numaralar = []
if __name__ == '__main__':
   logo(True)
   bilgi("[1] Txt Dosyasından Numaraları Al!")
   bilgi("[2] İşlemi Başlat")
   bilgi("[3] Çıkış Yap!")
   secim =0
   while secim == 3:
      try:
         secim = int(soru("[?] Seçim Yapın: "))
      except:
         noadded("[!] Lütfen Sadece Rakam Giriniz!")
         exit(1)
      if secim ==1:
         filedata=""
         with open("numaralar.txt") as file:
            filedata=file.read()
         try:
            filedata=filedata.split("\n")
         except:
            noadded("Txt dosya formatı hatalı!")
         basarili("Numaralar getirildi!")
      elif secim == 2:
         if numaralar.count() ==0:
            noadded("Önce numaraları getirin!");continue
         for i in numaralar:
            rnd = random.choice([1,2,3,2,1])
            if rnd==3:
               API_ID=18050036
               API_HASH= "7a6b295a342a443925b380a746f6c9d5"
            elif rnd==2:
               API_ID=13309079
               API_HASH= "3360efff8d25flb490e07819e7a5954c"
            else:
               API_ID= 19282067
               API_HASH="be6cea759cf66e0a20c8f70a0161dd86"

            print("[i] Hazır Keyler Kullanılıyor...")
            API_ID = 18050036
            #API_HASH = "014b35b6184100b085b0d0572f9b5103"
            API_HASH= "7a6b295a342a443925b380a746f6c9d5"
            client = InteractiveTelegramClient(StringSession(), API_ID, API_HASH,telefon=str(i))
      else:
         noadded("[!] Bilinmeyen seçim.")
   hata("Güle güle!")
