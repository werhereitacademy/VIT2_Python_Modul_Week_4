import os
import kitap_islemleri
import uye_islemleri
import json


def anaekran():
    ekran="""
    ----------------------------------------------------------------------------
    -                    HALK KUTUPHANEMIZE HOS GELDINIZ                       -
    -                                                                          -
    -   1-UYELIK ISLEMLERI  1                                                  -
    -   2-KITAP ISLEMLERI   2                                                  -
    -   3-CIKIS             0                                                  -
    -                                                                          -
    ----------------------------------------------------------------------------
    """
    print(ekran)
    
def uye_ekran():
    ekran="""
    ----------------------------------------------------------------------------
    -    UYELER       = 1         =        KITAP ODUNC VERME = 5               -
    -    UYE EKLEME   = 2         =        KITAP IADE        = 6               -
    -    UYE ARA      = 3         =        KITAP TAKIBI      = 7               -
    -    UYE SIL      = 4         =        CIKIS             = 0               -
    -                             =                                            -
    ----------------------------------------------------------------------------    
        """
    print(ekran)
    
def kitap_ekran():
    ekran="""
    ----------------------------------------------------------------------------
    -    KITAPLAR       = 1                                                    -
    -    KITAP EKLEME   = 2                                                    -   
    -    KITAP ARA      = 3                                                    -
    -    KITAP SIL      = 4                 CIKIS  = 0                         -
    -                                                                          -
    ----------------------------------------------------------------------------    
        """
    print(ekran)
    
    
    

while(True):
    try:
        anaekran()
        
        
        Secim=int(input("Lutfen yapmak istediginiz secimin kodunu girin : "))
        
        if Secim == 1:
            while(True):
                try:
                    uye_ekran()
                    
                    uye_secim=int(input("Islem seciniz : "))
                    if   uye_secim == 1 :
                        uyeler=uye_islemleri.uye_kontrol()
                        sayi=len(uyeler)
                        # print(sayi)
                    # print(type(veri))
                        say=0
                        for i in range(sayi):
                            
                            x=f"""   
                        "id":{uyeler[i]["id"]}
                        "Uye Adi":{uyeler[i]["Uye Adi"]},   
                        "Tel":{uyeler[i]["Tel"]}, 
                        "Adres":{uyeler[i]["Adres"]}
                        
                    """
                            say+=1
                            print(say,"==> ",x)
                        print(say," Adet Uyemiz vardir")
                        
                    elif uye_secim == 2 :
                        uye_adi=input("uye adi ve soyadi giriniz:")
                        tel=input("Telefon giriniz: ")
                        adres=input("Adres giriniz: ")
                        uye_islemleri.uye_ekle(uye_adi,tel,adres)
                        
                    elif uye_secim == 3 :
                        arama=input("Aranacak kisi veya id giriniz : ")
                        uye_islemleri.uye_ara(arama)
                    elif uye_secim == 4 :
                        sil=input("Silinecek isim veya Id giriniz :")
                        uye_islemleri.uye_sil(sil)
                    elif uye_secim == 5 :
                        uye_islemleri.kitap_odunc_verme()
                    elif uye_secim == 6 :pass
                    elif uye_secim == 7 :
                        odunc_kitaplar=uye_islemleri.takip_oku()
                        # print(odunc_kitaplar)
                        for i in odunc_kitaplar:
                            
                            guzel_json = json.dumps(i, indent=4,ensure_ascii=False)
                            print(guzel_json)
                    elif uye_secim == 0 :break
                except:
                    print("Yanlis giris Yaptiniz ")
            
        elif Secim ==2:
            while(True):
                try:
                    kitap_ekran()
                    
                    kitap_secim=int(input("Islem seciniz : "))
                    if   kitap_secim == 1 :
                        kitaplar=kitap_islemleri.oku()
                        sayi=len(kitaplar)
                        sayac=0
                        for i in range(sayi):
                            sayac+=1
                            x=f"""   
                            "Kitap_Adi":{kitaplar[i]["Kitap_Adi"]},  
                            "Yazar":{kitaplar[i]["Yazar"]}, 
                            "Yayinevi":{kitaplar[i]["Yayinevi"]},
                            "Barkod":{str(kitaplar[i]["Barkod"])} 
                            
                            """
                            
                            print(sayac,"===>",x)
                        print(sayac," Adet Kutuphanemizde Kitap vardir")  

                    elif kitap_secim == 2 :
                        
                        Kitap_Adi=input("Kitap_Adi giriniz : ")
                        Yazar=input("Yazar giriniz : ")
                        Yayinevi=input("Yayinevi giriniz : ")
                        Barkod=input("Barkod giriniz : ")
                        kitap_islemleri.kitap_ekle(Kitap_Adi,Yazar,Yayinevi,Barkod)
                        
                        
                    elif kitap_secim == 3 :
                        arama=input("Aranacak Kitap_Adi|Yazar|Yayinevi|Barkod giriniz : ")
                        kitap_islemleri.kitap_ara(arama)
                    elif kitap_secim == 4 :
                        sil=input("Silinecek Kitap_Adi|azar,Yayinevi|Barkod giriniz :")
                        kitap_islemleri.kitap_sil(sil)
                    elif kitap_secim == 0:break
                except:
                    print("Yanlis giris yaptiniz ")
                          
            
        elif Secim == 0:
            quit()
            
    except Exception as hata:
        print("Muhtemelen yanlis giris yaptiniz :  ",hata,end='\n\n')       

