
##############################Kutuphane Projesi#################################



###Main.py###
import kitap_islemleri
import uye_islemleri
import json
import os


while(True):
    try:
        print("--------------------------------------------")
        print("-    HALK KUTUPHANEMIZE HOS GELDINIZ       -")
        print("-       1 - UYELIK ISLEMLERI = 1           -")
        print("-       2 - KITAP ISLEMLERI = 2            -")
        print("-       3 - CIKIS = 0                      -")
        print("--------------------------------------------")
        secim=input("Lutfen yapmak istediginiz secimin numarasini girin : ", )
        os.system('cls')
        if secim == '1': 
            while True:
                print("---------------------------------------------------------")
                print("-   UYELER = 1                 KITAP ODUNC VERME = 5    -")
                print("-   UYE EKLEME = 2             KITAP IADE = 6           -")
                print("-   UYE ARA = 3                KITAP TAKIBI = 7         -")
                print("-   UYE SIL = 4                CIKIS = 0                -")
                print("---------------------------------------------------------")
                uye_secim=input("Lutfen yapmak istediginiz secimin numarasini girin : ", )
                if uye_secim=="1": 
                    uye_islemleri.uye_listeleme()
                elif uye_secim=="2": 
                    uye_islemleri.uye_ekle()
                elif uye_secim=="3": 
                    uye_islemleri.uye_ara()
                elif uye_secim=="4": 
                    uye_islemleri.uye_sil()
                elif uye_secim=="5": 
                    uye_islemleri.kitap_odunc_verme()
                elif uye_secim=="0": 
                    break

        elif secim == '2':
            while True:
                print("--------------------------------")
                print("-       KITAPLAR = 1           -")
                print("-      KITAP EKLEME = 2        -")
                print("-      KITAP ARA = 3           -")
                print("-      KITAP SIL = 4           -")
                print("-      CIKIS = 0               -")
                print("--------------------------------")
                kitap_secim=input("Lutfen yapmak istediginiz islemin numarasini giriniz : " )
                if kitap_secim=="1": 
                    kitap_islemleri.kitaplar()
                elif kitap_secim=="2":
                    kitap_islemleri.kitap_ekle(Kitap_Adi, Yazar, Yayinevi, Barkod)
                elif kitap_secim=="3": 
                    kitap_islemleri.kitap_ara(ara)
                elif kitap_secim=="4": 
                    kitap_islemleri.kitap_sil(silinecek_kitap.lower())
                elif kitap_secim=="0": 
                    break    
        elif secim == '0':
            print("Cikis yapiliyor!...")
            break

    except Exception as hata:
        print("Hata : ", hata, end='\n\n')

###Uye_islemleri.py###

import kitap_islemleri
import json
import os
import zaman




try:
    with open("uye.json", "r", encoding="utf-8") as json_dosyasi:
        Uyeler = json.load(json_dosyasi)
except FileNotFoundError:
    Uyeler = []

def uye_kontrol():
    with open('uye.json', 'r',encoding="utf-8") as dosya:
        json_verileri = dosya.read()
    if json_verileri is not None:
        uyeler = json.loads(json_verileri)
    return uyeler

def uye_ekle():
    Uye_Adi = input("Uye adi giriniz : ")
    Tel = input("Uye telefon giriniz : ")
    Adres = input("Uye adres giriniz : ")
    Uye = {
        "Id":  max(uye['Id'] for uye in Uyeler) + 100,
        "Uye Adi": Uye_Adi,
        "Telefon": Tel,
        "Adres": Adres}
    Uyeler.append(Uye)
    print(f"{max(uye['Uye Adi'] for uye in Uyeler)} id numarali {Uye_Adi} uyesi eklendi.")
    with open("uye.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(Uyeler, json_dosyasi, ensure_ascii=False, indent=3)

def uye_listeleme():
    for uye in Uyeler:
        print(uye)
    print("Uye sayisi= ", len(Uyeler))

def uye_ara():
    ara= input("Uye adi yada id giriniz : ")
    for uye in Uyeler:
        if ara==uye["Uye Adi"] or ara==str(uye["Id"]):
            print(uye)
            break
    else:
        print("Kayit Bulunamadi.")

def uye_sil():
    silinecek_uye = int(input("Silinecek Uye Id: "))
    for uye in Uyeler:
        if uye["Id"] == silinecek_uye:
            Uyeler.remove(uye)
            print(f"'{uye['Uye Adi']}' isimli uye silindi.")
            break
    else:
        print("Uye kaydi bulunamadi")
    with open("uye.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(Uyeler, json_dosyasi, ensure_ascii=False, indent=4)

def takip_yaz(veri):
    with open('takip.json', 'w',encoding="utf-8") as json_dosya:
        json.dump(veri, json_dosya ,indent=3,ensure_ascii=False)
        print("Kitap Takip Verileri Guncellendi.")

def takip_oku():
    with open('takip.json', 'r',encoding="utf-8") as dosya:
        json_verileri = dosya.read()
def kitap_odunc_verme():
    aranan_kitap=input("Hangi kitap isteniyor ==> : ").lower()
    istek=kitap_islemleri.kitap_ara(aranan_kitap)
    try:
        if istek!=[]:
            barkod=input(" Kitabin Barkod Numarasini Giriniz : ")
            odunc_kitap=kitap_islemleri.kitap_ara(barkod)
            if odunc_kitap!=[]:                
                musteri=input("Musterinin Adi , veya Id ").lower()
                uyeler=uye_kontrol()
                sayi=len(uyeler)
                sonuc=[]
                for i in range(sayi):

                    if musteri == uyeler[i]["Uye Adi"].lower() or musteri == str(uyeler[i]["Id"] )  :

                        x=f"""   
                        "Id":{uyeler[i]["Id"]},
                        "Uye Adi":{uyeler[i]["Uye Adi"]},   
                        "Tel":{uyeler[i]["Tel"]}, 
                        "Adres":{uyeler[i]["Adres"]}            
                        """
                        print(x)
                        sonuc.append(uyeler[i])
                        break

                if sonuc==[]:
                    print("Bu isimde Kayit Bulunmamaktadir")
                else:
                    dosya_adi = "takip.json"
                    if os.path.exists(dosya_adi):
                        su_an,bitis_tarihi=zaman.tarih()
                        tarih={"Kayit Tarihi":su_an,"Kitap iade Tarihi":bitis_tarihi}
                        odunc_verisi = {**sonuc[0],**odunc_kitap[0],**tarih}
                        print(odunc_verisi)
                        oku=takip_oku()
                        oku.append(odunc_verisi)  
                        takip_yaz(oku)  
                        up_date=kitap_islemleri.oku()     
                        up_date.remove(odunc_kitap[0])  
                        kitap_islemleri.kayit(up_date)
                    else:
                        print("takip dosyasi ilk kurulum icin hazilaniyor sonra tekrar deneyin",end='\n')
                        takip_yaz([])
            else:

                print("Barkod Yanlis veya Kitap Odunc Verildi",end='\n')
        else:
            print("Bu kitap elimizde yok",end='\n')
    except Exception as hata:
        print("Lutfen Verileri dogru girdiginizden emin olun. Hata: ",hata)


#Kitap_islemleri.py
import json
import os

try:
    with open("kitap.json", "r", encoding="utf-8") as json_dosyasi:
        Kitaplar = json.load(json_dosyasi)
except FileNotFoundError:
    Kitaplar = []

def kayit(veri):
    with open("kitap.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(Kitaplar , json_dosyasi, ensure_ascii=False, indent=4)

def kitaplar():
    for kitap in Kitaplar:
        print(kitap)
    print("Kitap Sayisi= ", len(Kitaplar))

def kitap_ekle(Kitap_Adi, Yazar, Yayinevi, Barkod):
    Kitap_Adi = input("Kitap adi giriniz : ")
    Yazar = input("Yazar giriniz : ")
    Yayinevi = input("Yayinevi giriniz : ")
    Barkod = input("Barkod giriniz : ")
    kitap = {
        "Barkod": Barkod,
        "Dil": "Türkçe",
        "Fiyat": 0,
        "Kitap_Adi": Kitap_Adi,
        "Yayinevi": Yayinevi,
        "Yazar": Yazar
    }
    Kitaplar.append(kitap)
    print(f"{kitap['Barkod']} barkodlu {Kitap_Adi} eklendi.")
    with open("kitap.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(Kitaplar, json_dosyasi, ensure_ascii=False, indent=4)

def kitap_sil(silinecek_kitap):
    silinecek_kitap = input("Silinecek kitabin adi: ")
    for kitap in Kitaplar:
        if kitap["Kitap_Adi"].lower() == silinecek_kitap:
            Kitaplar.remove(kitap)
            print(f"'{kitap['Kitap_Adi']}' isimli kitap silindi.")
            break
    else:
        print("Kitap bulunamadi.")
    with open("kitap.json", "w", encoding="utf-8") as json_dosyasi:
        json.dump(Kitaplar, json_dosyasi, ensure_ascii=False, indent=4)
    pass

def kitap_ara(ara):
    ara= input("Aranilan kitabin adi : ")
    bulunan_kitap=[]
  
    for kitap in Kitaplar:
        if ara.lower() in kitap["Kitap_Adi"].lower() or ara in str(kitap["Barkod"]):
            bulunan_kitap.append(kitap)

    print(*bulunan_kitap, sep="\n")

    if len(bulunan_kitap)==0 :
        print("Kitap bulunmadi")


#takip.json

from datetime import datetime, timedelta
import json

def tarih():
    simdiki_zaman = datetime.now()
    iade_tarihi = simdiki_zaman + timedelta(week=2)


    simdiki_zaman_str = simdiki_zaman.strftime("%d-%m-%Y %H:%M")
    iade_tarihi_str = iade_tarihi.strftime("%d-%m-%Y")


    kitap_bilgisi = {
        "odunc_tarihi": simdiki_zaman_str,
        "iade_tarihi": iade_tarihi_str
    }
    with open("takip.json", "w") as json_dosyasi:
        json.dump(kitap_bilgisi, json_dosyasi)
    return f"alinan tarih : {simdiki_zaman_str}, | bitis tarihi: {iade_tarihi_str}"


#print("alinan tarih :", simdiki_zaman_str, " | ", "iade tarihi:", iade_tarihi_str)


if __name__ == "__main__":
    print(tarih())
