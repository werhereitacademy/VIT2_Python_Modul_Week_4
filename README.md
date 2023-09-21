# VIT2 Python-Module-Week4
## Kutuphane Projesi
- Bu projede şu ana kadar öğrendiğiniz python bilgilerinizle beraber hata yakalama - dosya işlemleri  özellikle Json modulu ve dosya bilgisini kullanılarak bir kütüphane programı yazmanızı istiyoruz.
- Bir kutuphanede; Uyelik islemleri, Kitap islemleri  olmak uzere iki ana kısım vardır.
- Uyelik işlemleri içerisinde üye ekleme, üye silme, üye kontrolü, üyeye kitap verme, üyeden iade kitap alma bilgisi bulunmaktadır. Bir de üyelik verisinin kaydedildigi bir database veya dosya gerekmektedir. 
- Kitap işlemleri içinde benzer şeyleri söyleyebiliriz.

#### Projeyi detaylandıracak olursak:
 * main.py, kitap_işlemleri.py,üye_işlemleri.py, zaman.py  dosyalarindan oluşacak.
##### Main.py:
* Projemizi ana dosyası main.py dosyası olacak. işlemler bu dosyadan yürütülecek diğer Python dosyaları bir modül olarak bu bölümden çağrılacak . Örneğin kitap ekleme kitap silme ,üye ekleme , üyeye kitap verme ,üye kontrolü buradan yapılacak.
 ![resim](https://github.com/werhereitacademy/week_4/assets/141542413/fd0ea3eb-d5cc-4991-b67d-94ebf42ee8d9)

* Aşağıda bu projenin çalıştırılmış bir çıktısını göreceksiniz. Main sayfasında inputlar araciligiyla ile kitap_işlemleri ve üyelik_işlemleri modüllerindeki fonksiyonları çalıştırabilirsiniz.
  ![resim](https://github.com/werhereitacademy/week_4/assets/141542413/7708052f-5b9c-42ed-b4c0-1a6e92d5fbf6)
##### kitap_işlemleri.py :
* Bu modulde kitap bilgisi(kayitli kitaplar ve toplam adeti), ekleme,silme,arama,update fonksiyonlarini yazacaksiniz. Verilerimizi kitap.json dosyasina kaydedecegiz. Kitap.json dosyasi size hazir verilecek (dileyen kendide olusturabilir). Os Modulu ile dosya kontrolu mutlaka yapilmalidir. Aşağıda kitap işlemleri için fonksiyon örneklemeleri bulabilirsin fakat buna uymak zorunda değilsiniz, kendi planlamanızı da yapabilirsiniz.
## Hackerrank Questions

1. Diagonal Difference: https://www.hackerrank.com/challenges/diagonal-difference/problem

2. Left Rotation: https://www.hackerrank.com/challenges/array-left-rotation/problem

3. Counter game: https://www.hackerrank.com/challenges/counter-game/problem

4. Time Delta: https://www.hackerrank.com/challenges/python-time-delta/problem
