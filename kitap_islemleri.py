import kitap_islemleri
import json
import os

# Musterinin kitabi aldigi tarih ve teslim tarihi verisini isle
import zaman
# ===========================================================================
# Uye.json dosyasi yazma olusturma
def uye_guncelle(uye):
    with open('uye.json', 'w',encoding='utf-8') as json_dosya:
        json.dump(uye, json_dosya ,indent=3,ensure_ascii=False)
        # Şimdi veriyi kullanabilirsiniz
        print("------------------------------------------------------")
        print(" Uyeler Guncellendi.",end='\n')

# =========================================================================== 
# Uye.json dosyasi yazma olusturma
def uye_kontrol():
    with open('uye.json', 'r',encoding="utf-8") as dosya:
        json_verileri = dosya.read()
        # print(type(json_verileri))
    
    # JSON verilerini bir Python veri yapısına dönüştürün (genellikle bir sözlük veya liste)
        if json_verileri is not None:
            uyeler = json.loads(json_verileri)
            
    return uyeler

# ===========================================================================    
# uye ekle
def uye_ekle(Uye_Adi,Tel,Adres):
    dosya_kontrol = "uye.json"
    # dosya kontrolu 
    if os.path.exists(dosya_kontrol):
        # print(f"{dosya_adı} basariyla yuklendi.")
        yeni_uye=uye_kontrol()
        # print(yeni_uye)
        
        yeni_uye_veri = {
        "id":len(yeni_uye)+117,
        "Uye Adi":Uye_Adi,   
        "Tel":Tel, 
        "Adres":Adres}
        
        yeni_uye.append(yeni_uye_veri)
        uye_guncelle(yeni_uye)
    
    else:
        print(f"{dosya_kontrol} dosya olusturuluyor.",end='\n')
        uye_guncelle([])

# ===========================================================================        
# uye arama
def uye_ara(arama):
    uyeler=uye_kontrol()
    sayi=len(uyeler)
    sayac=0
    # print(sayi)
    aranan_uyeler=[]
    for i in range(sayi):
        if arama in uyeler[i]["Uye Adi"].lower() or arama in uyeler[i]["Adres"].lower() or arama in str(uyeler[i]["id"]) :
            sayac+=1
            x=f"""   
        "id":{uyeler[i]["id"]}
        "Uye Adi":{uyeler[i]["Uye Adi"]},   
        "Tel":{uyeler[i]["Tel"]}, 
        "Adres":{uyeler[i]["Adres"]}
        
        """
            print(sayac,"==> ",x)
            aranan_uyeler.append(uyeler[i])
    return aranan_uyeler    

# ===========================================================================
# uye silme
def uye_sil(silinecek_uye):
    uyeler=uye_kontrol()
    kalan_uye=uyeler.copy()
    sayi=len(uyeler)
    sayac=0
    # print(sayi)
    sil=[]
    for i in range(sayi):
        if silinecek_uye in uyeler[i]["Uye Adi"].lower() or silinecek_uye in str(uyeler[i]["id"]) :
            # print(veri_oku[i])
            
            x=f"""   
        "id":{uyeler[i]["id"]},
        "Uye Adi":{uyeler[i]["Uye Adi"]},   
        "Tel":{uyeler[i]["Tel"]}, 
        "Adres":{uyeler[i]["Adres"]}
        
        """
            print(sayac,"> ",x)
            sayac+=1
            sil.append(uyeler[i])
            
    # print(sil)
    try:
        x=int(input("silmek istediginiz verinin indexsini giriniz : "))
        f=sil[x]
        kalan_uye.remove(f)
        uye_guncelle(kalan_uye)
        print("Veriler Basariyla Silindi")
    except:
        print("Lutfen dogru index girin")
        print("Veriler silinemedi....")
    
    # print(len(kalan_veri))
# ===========================================================================
# uye okuyucuya kitap verme (tarih islemlerini burada yapacaksin)
def kitap_odunc_verme():
    
    aranan_kitap=input("Hangi kitap isteniyor ==> : ").lower()
    istek=kitap_islemleri.kitap_ara(aranan_kitap)
    try:
        # print(istek)
        if istek!=[]:
            
            barkod=input(" Kitabin Barkod Numarasini Giriniz : ")
            odunc_kitap=kitap_islemleri.kitap_ara(barkod)
            # print("odunc",odunc_kitap)
            
            if odunc_kitap!=[]:                
                musteri=input("Musterinin Adi , veya id ").lower()
                uyeler=uye_kontrol()
                sayi=len(uyeler)
                # print(sayi)
                sonuc=[]
                for i in range(sayi):
                                    
                    if musteri == uyeler[i]["Uye Adi"].lower() or musteri == str(uyeler[i]["id"] )  :
                        
                        x=f"""   
                        "id":{uyeler[i]["id"]},
                        "Uye Adi":{uyeler[i]["Uye Adi"]},   
                        "Tel":{uyeler[i]["Tel"]}, 
                        "Adres":{uyeler[i]["Adres"]}            
                        """
                        print(x)
                        sonuc.append(uyeler[i])
                        break
                
                if sonuc==[]:
                    print("Bu isimde Kayit Bulunmamaktadir Lutfen Kayit olunuz ")
                    
                else:
                    # print(sonuc)
                    dosya_adı = "takip.json"
            # dosya kontrolu 
                    if os.path.exists(dosya_adı):
                        su_an,bitis_tarihi=zaman.tarih()
                        tarih={"Kayit Tarihi":su_an,"Kitap iade Tarihi":bitis_tarihi}
                        # print(su_an,bitis_tarihi)
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
    # Diğer tüm hataların (Exception) yakalandığında yapılacaklar
        print("Lutfen Verileri dogru girdiginizden emin olun. Hata: ",hata)

# ===========================================================================
# takip.json dosyasini burada olusturup yazacaksin
def takip_yaz(veri):
    with open('takip.json', 'w',encoding="utf-8") as json_dosya:
        json.dump(veri, json_dosya ,indent=3,ensure_ascii=False)
        # Şimdi veriyi kullanabilirsiniz
        print("Kitap Takip Verileri Guncellendi.")

# ===========================================================================
# takip.json dosyasini buradan okuyacaksin
def takip_oku():
    with open('takip.json', 'r',encoding="utf-8") as dosya:
        json_verileri = dosya.read()
    # print(type(json_verileri))

# JSON verilerini bir Python veri yapısına dönüştürün (genellikle bir sözlük veya liste)
        if json_verileri is not None:
            veri = json.loads(json_verileri)
    # print(type(veri))
        return veri

# ===========================================================================
def kitap_iade():pass

if __name__ == '__main__':
    kitap_odunc_verme()
