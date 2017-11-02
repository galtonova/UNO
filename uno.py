import random
import os
from time import sleep

# Kart türlerine sayı verip bunları ezberlememek
# için yaptığım bir garip şey
class KartTurleri:
    # Kart Renkleri
    # Siyah renk Joker kartlar
    siyah = 0
    kirmizi = 1
    sari = 2
    yesil = 3
    mavi = 4

    # Kart Değerleri
    # 0,1,2,3,4,5,6,7,8,9 Normal Kartlar
    # 10,11,12,13,14 Özel Kartlar
    pas_gec = 10
    yon_degistirici = 11
    arti2 = 12
    renk_degistirici = 13
    arti4 = 14
# end of class KartTurleri


# Kart sınıfı
# print fonksiyonunda vb. kullanmak için,
# __str__ methodu sayesinde direk
# str( obje ) şeklinde str'ye dönüştürülebiliyor.
# renk ve değer özellikleri var,
# renk olan rengi (ne kadar ilginç!)
# değer olan da rengin üzerinde yazan/çizilen şeysisi
#
# constructor ( __init__ ) iki parametre alıyor: renk ve değer
# değişken = Kart(xx,xx) şeklinde oluşturuluyor
class Kart:
    renk = 0
    deger = 0

    def __str__(self):
        #return "{renk:" + str(self.renk) + ", deger:" + str(self.deger).zfill(2) + "}"
        t = ""
        if self.renk == KartTurleri.kirmizi:
            t += "Kırmızı"
        elif self.renk == KartTurleri.sari:
            t += "Sarı   "
        elif self.renk == KartTurleri.yesil:
            t += "Yeşil  "
        elif self.renk == KartTurleri.mavi:
            t += "Mavi   "
        elif self.renk == KartTurleri.siyah:
            t += "Renksiz"

        t += " / "

        if self.deger == KartTurleri.pas_gec:
            t += "Pas Geç"
        elif self.deger == KartTurleri.yon_degistirici:
            t += "Yön Değiştirici"
        elif self.deger == KartTurleri.arti2:
            t += "+2"
        elif self.deger == KartTurleri.renk_degistirici:
            t += "Renk Değiştirici"
        elif self.deger == KartTurleri.arti4:
            t += "+4"
        else:
            t += str(self.deger)
        return t

    def __init__(self, r, d):
        self.renk = r
        self.deger = d
# end of class Kart

# Deste sınıfı
# içinde  bir adet deste dizisi var
# ve desteyi kontrol eden bir yığın fonksiyon var
class Deste:
    deste = []

    # Destenin içine kartları koyup karıştırır
    def yeni_karisik_deste(self):
        self.deste = []
        # 0,1,2,3,4,5,6,7,8,9,pas geç(10),yön değiştirici(11), +2(12)
        for i in range(13):
            self.deste.append(Kart(KartTurleri.kirmizi, i))
        for i in range(13):
            self.deste.append(Kart(KartTurleri.sari, i))
        for i in range(13):
            self.deste.append(Kart(KartTurleri.yesil, i))
        for i in range(13):
            self.deste.append(Kart(KartTurleri.mavi, i))

        # 1,2,3,4,5,6,7,8,9,pas geç(10),yön değiştirici(11), +2(12)
        for i in range(1, 13):
            self.deste.append(Kart(KartTurleri.kirmizi, i))
        for i in range(1, 13):
            self.deste.append(Kart(KartTurleri.sari, i))
        for i in range(1, 13):
            self.deste.append(Kart(KartTurleri.yesil, i))
        for i in range(1, 13):
            self.deste.append(Kart(KartTurleri.mavi, i))

        # renk değiştirici(13), +4(14)
        for i in range(4):
            self.deste.append(Kart(KartTurleri.siyah, 13))
        for i in range(4):
            self.deste.append(Kart(KartTurleri.siyah, 14))

        random.shuffle(self.deste)

    # UNO Kurallarından direk alıntı:
    #   İlk çekilen kart +4 ya da Renk Değiştirici olamaz.
    #
    #   Eğer ilk kart +4 ya da Renk Değiştirici çıkarsa,
    # kartın desteye geri koyulup tüm destenin karıştırılması
    # ve yeniden ilk kartın çekilmesi gerekir
    #   +4 ve Renk Değiştirici hariç tüm kartlar ilk kart olabilir
    def ilk_karti_cek(self):
        # saçma sapan işler yapmak yerine
        # destedeki ilk +4 / RenkDeğiştirici olmayan kartı al
        for k in self.deste:
            if k.deger != KartTurleri.arti4 and k.deger != KartTurleri.renk_degistirici:
                return k

    # Destenin en üstündeki kartı geriye döndürür ve diziden siler.
    # Eğer deste içerisinde eleman kalmazsa, yerdekiler parametresiyle
    # gelen diziyi alır, onun en üstündeki kartı (ortadaki) ayırır ve kalanları
    # karıştırıp bu destenin sonuna ekler
    # n parametresiyle birden fazla kart çekilebilir. Kart dağıtırken 7 vermek gibi
    def kart_cek(self, n=1, yerdekiler=False):
        if len(self.deste) <= n:
            print("YERDEKİ DESTE KARIŞTIRILIP ANA DESTEYE İLAVE EDİLİYOR...")
            if not yerdekiler:
                print("YERDEKİLERİ KART ÇEK İÇİNE PARAMETRE OLARAK VERİN!")
                exit(0)
            ustteki = yerdekiler.ustteki()
            del yerdekiler.deste[0]
            yerdekiler.karistir()
            for yerdeki in yerdekiler.deste:
                self.deste.append(yerdeki)
            #del yerdekiler.deste
            yerdekiler.deste = []
            yerdekiler.uste_kart_koy(ustteki)

        if n == 1:
            t = self.deste[0]
            del self.deste[0]
            return t
        kartlar = []
        for i in range(n):
            kartlar.append(self.deste[0])
            del self.deste[0]
        return kartlar


    # Bunlar da yerdeki kart destesi için

    # Destenin en üstündeki elemanı verir ama silmez
    def ustteki(self):
        return self.deste[0]

    # Destenin en üstüne kart  ekler
    def uste_kart_koy(self, kart):
        self.deste.insert(0, kart)

    # Tüm desteyi karıştırır
    def karistir(self):
        random.shuffle(self.deste)
# end of class Deste


# Oyuncu sınıfı
# Oyuncuların adı var,
# elindeki kartların olduğu el dizisi var,
# bir de insan mı bilgisayar mı değişkeni var
class Oyuncu:
    insan = False
    el = []
    isim = ""

    # kartlar parametresiyle gelen kartları el içine aktarır
    def yeni_el(self, kartlar):
        self.el = kartlar

    # kart parametresiyle gelen kartı ele ekler (kart çekme işlemi için)
    def kart_ver(self,kart: Kart):
        self.el.append(kart)

    # oyuncunun sırası geldiğinde burası çalışacak
    def oyna(self, ortadaki, ikinci=False):
        print("SIRADAKİ OYUNCU:", self.isim,"["+str(len(self.el))+"]")
        if self.insan:
            print("Ortadaki:",ortadaki)

        while True:
            secim = 0
            if self.insan:
                if not ikinci:
                    print(" 0. Kart Çek")
                else:
                    # Eğer kart çekmişsek, tekrar kart çekemeyeceğiz
                    print(" 0. Pas")
                for i, kart in enumerate(self.el):
                    # Kart atılabilirse, başına index+1 i yazacağız
                    if ortadaki.renk == kart.renk or ortadaki.deger == kart.deger or kart.renk == KartTurleri.siyah:
                        # Print yaparken daha güzel görünsün diye, 10 dan küçükse sayının başına boşluk koydurdum
                        if i + 1 >= 10:
                            print(str(i + 1) + ". " + str(kart))
                        else:
                            print(" "+str(i + 1) + ". " + str(kart))
                    else:
                        # Kartı atamıyorsak boşluk olacak sadece
                        print("    " + str(kart))
                secim = int(input("Kart No: "))-1
            else:
                # Bilgisayarın kart seçme mantığı
                secilebilecekler = []
                jokerler = []
                for k in range( len(self.el) ):
                    kart = self.el[k]
                    # Eğer normal bir kartsa ve atılabiliyorsa secilebilecekler dizisine koy
                    if ortadaki.renk == kart.renk or ortadaki.deger == kart.deger:
                        secilebilecekler.append(k)
                    # Eğer joker kartsa (siyah) jokerlere koy (+4 ve renk değiştirme)
                    elif kart.renk == KartTurleri.siyah:
                        jokerler.append(k)
                # Eğer secilebilecekler dizisinde eleman varsa
                # Onu seç
                if len(secilebilecekler) > 0:
                    secim = secilebilecekler[random.randint(0,len(secilebilecekler)-1)]
                # secilebilecekler dizisinde eleman yoksa joker seç
                elif len(jokerler) > 0:
                    secim = jokerler[random.randint(0, len(jokerler) - 1)]
                # jokerler dizisinde de eleman yoksa kart çek / pas geç
                else:
                    secim = -1

            secilen = self.el[secim]

            if secilen.renk == KartTurleri.siyah:
                renk = ""
                if self.insan:
                    renk = input("Yeni Renk: ")
                else:
                    # Bilgisayarın joker sonrası renk seçim mantığı
                    # Elindeki kartlarda hhangi renkten en çok varsa
                    # Onu seçer
                    yesiller = 0
                    maviler = 0
                    kirmizilar = 0
                    sarilar = 0
                    for kart in self.el:
                        if kart.renk == KartTurleri.yesil:
                            yesiller += 1
                        elif kart.renk == KartTurleri.mavi:
                            maviler += 1
                        elif kart.renk == KartTurleri.kirmizi:
                            kirmizilar += 1
                        elif kart.renk == KartTurleri.sari:
                            sarilar += 1
                    ls = [yesiller, maviler, kirmizilar, sarilar]
                    ls.sort()

                    if ls[3] == yesiller:
                        renk = "yeşil"
                    elif ls[3] == maviler:
                        renk = "mavi"
                    elif ls[3] == kirmizilar:
                        renk = "kırmızı"
                    elif ls[3] == sarilar:
                        renk = "sarı"
                # Yanlış yazmalarla uğraşmamak için,
                # Girilen renk stringinin sadece ilk karakterine bak (küçük harfe çevirip)
                if renk[0].lower() == "m":
                    renk = KartTurleri.mavi
                elif renk[0].lower() == "s":
                    renk = KartTurleri.sari
                elif renk[0].lower() == "y":
                    renk = KartTurleri.yesil
                elif renk[0].lower() == "k":
                    renk = KartTurleri.kirmizi

                # eldeki seçilen kartı sil, geriye de atılacak kartı, yeni girilen renkle döndür
                # ör. Renksiz  +4, Mavi +4 olacak vs.
                del self.el[secim]
                return Kart(renk, secilen.deger)
            # Kart atılabiliyorsa, kartı el'den sil, ve geriye döndür
            elif ortadaki.renk == secilen.renk or ortadaki.deger == secilen.deger:
                del self.el[secim]
                return secilen
            # Eğer kart çek / pas seçildiyse -1 döndür
            elif secim == -1:
                return -1
    # end of def oyna
# end of class oyuncu


# Bu da asıl oyun mekaniklerinin olduğu class
# ana_deste kart çekme destesi
# yerdeki_deste ortaya atılan kartların olduğu deste
# oyuncular dizisi,  oyuncular
# sıradaki, bir sonraki oyuncunun indexi (bir oyuncu atlama vs için)
# yon de +1 mi yoksa -1 mi gideceği (yön değiştirme kartı bunu değiştirecek)
class Oyun:
    ana_deste = Deste()
    yerdeki_deste = Deste()
    oyuncular = []
    siradaki = -1
    yon = 1

    # yeni oyun açar
    # n: rakip sayısı
    def yeni(self, n=3):
        # Yeni karışık deste oluştur
        self.ana_deste.yeni_karisik_deste()

        # Oyuncuları ekle (n rakip, bir insan) ve ellerini dağıt
        for i in range(n+1):
            yeni_oyuncu = Oyuncu()
            yeni_oyuncu.yeni_el(self.ana_deste.kart_cek(7))
            yeni_oyuncu.isim = "Oyuncu "+str(i)
            self.oyuncular.append(yeni_oyuncu)
        self.oyuncular[0].insan = True

        # İlk kartı çekip yerdeki desteye koy
        self.yerdeki_deste.uste_kart_koy(self.ana_deste.ilk_karti_cek())

    # Ortadaki karta göre işlem yap
    # Bunu ayırdım ki bir sefr yapsın
    def ortayi_degerlendir(self):
        ortadaki = self.yerdeki_deste.ustteki()

        if ortadaki.deger == KartTurleri.pas_gec:
            self.siradaki += self.yon
            self.siradaki = self.siradaki % len(self.oyuncular)
            print(self.oyuncular[self.siradaki].isim,"Pas Geçildi")

        elif ortadaki.deger == KartTurleri.yon_degistirici:
            print("Yön Değiştirildi.",
                  self.oyuncular[(self.siradaki+self.yon) % len(self.oyuncular)].isim,
                  "Yerine",
                  self.oyuncular[(self.siradaki-self.yon) % len(self.oyuncular)].isim,
                  "Oynayacak")
            self.yon = -self.yon

        elif ortadaki.deger == KartTurleri.arti2:
            self.siradaki += self.yon
            self.siradaki = self.siradaki % len(self.oyuncular)
            self.oyuncular[self.siradaki].kart_ver(self.ana_deste.kart_cek(1,self.yerdeki_deste))
            self.oyuncular[self.siradaki].kart_ver(self.ana_deste.kart_cek(1,self.yerdeki_deste))
            print(self.oyuncular[self.siradaki].isim, " Pas Geçti ve İki Kart Çekti")

        elif ortadaki.deger == KartTurleri.arti4:
            self.siradaki += self.yon
            self.siradaki = self.siradaki % len(self.oyuncular)
            self.oyuncular[self.siradaki].kart_ver(self.ana_deste.kart_cek(1,self.yerdeki_deste))
            self.oyuncular[self.siradaki].kart_ver(self.ana_deste.kart_cek(1,self.yerdeki_deste))
            self.oyuncular[self.siradaki].kart_ver(self.ana_deste.kart_cek(1,self.yerdeki_deste))
            self.oyuncular[self.siradaki].kart_ver(self.ana_deste.kart_cek(1,self.yerdeki_deste))
            print(self.oyuncular[self.siradaki].isim, " Pas Geçti ve Dört Kart Çekti")

    # Oyunu başlat ve sürekli sıradaki oyuncuyu çalıştır
    def baslat(self):
        print("YENİ OYUN BAŞLADI")
        print("---------------------------")
        print(self.yerdeki_deste.ustteki())
        print("---------------------------")
        self.ortayi_degerlendir()
        self.siradaki += self.yon
        input("Devam etmek için Enter'a basınız...")
        while True:
            # Geriye True dönerse oyunu biri kazanmış demektir, çık döngüden
            if self.siradaki_oyuncu():
                break

    # sıradaki oyuncu işlemleri
    def siradaki_oyuncu(self):
        # sıradaki oyuncu 0 ın altına ya da oyuncu sayının üstüne çıkarsa
        # onu döndürüyoruz
        self.siradaki = self.siradaki % len(self.oyuncular)

        # Eğer sıradaki oyuncu insansa, ekranı temizle
        if self.oyuncular[self.siradaki].insan:
            os.system('cls' if os.name == 'nt' else 'clear')

        #  destede kalan kart sayısı ve oyuncuların ellerindeki kart sayılarını yaz
        print("---------------------------")
        print("deste:", str(len(self.ana_deste.deste)), end='')
        for o in range(len(self.oyuncular)):
            print(" o", str(o), ":", str(len(self.oyuncular[o].el)), sep='', end='')
        print("\n---------------------------")

        # sıradaki oyuncu oynat.
        # geriye kart dönerse onu atmış demek.
        # geriye -1 dönerse kart çekecek demek.
        # zaten kart çekmişse ve yine -1 dönerse de pas geçecek
        kart = self.oyuncular[self.siradaki].oyna(self.yerdeki_deste.ustteki())
        if kart == -1:
            # oyuncu kart çekmek istiyor
            sleep(0.5)
            print(self.oyuncular[self.siradaki].isim, "Kart Çekti")
            self.oyuncular[self.siradaki].kart_ver(self.ana_deste.kart_cek(1,self.yerdeki_deste))
            kart = self.oyuncular[self.siradaki].oyna(self.yerdeki_deste.ustteki(),True)

        # Eğer üstte ona kart vermemize rağmen hala -1 döndürüyorsa
        # Pas geçir
        if kart == -1:
            # oyuncu kart atmadı
            print(self.oyuncular[self.siradaki].isim,"Kart Atmadı")
        else:
            # oyuncu kart attı
            print(self.oyuncular[self.siradaki].isim,"Kart Attı")
            print("Atılan Kart:",kart)
            self.yerdeki_deste.uste_kart_koy(kart)

            # Elindeki kartlar bittiyse
            if len(self.oyuncular[self.siradaki].el) == 0:
                print("---------------------------")
                print(self.oyuncular[self.siradaki].isim," KAZANDI!")
                print("---------------------------")
                return True
            # Elinde tek kart kaldıysa
            elif len(self.oyuncular[self.siradaki].el) == 1:
                print("---------------------------")
                print(self.oyuncular[self.siradaki].isim, " UNO!")
                print("---------------------------")
            self.ortayi_degerlendir()
        # Sıradaki oyuncu index'ini yön kadar artır.
        self.siradaki += self.yon
        # Her şey akıp gitmesin diye Enter'a basınca geçecek şekle getirdim
        input("Devam etmek için Enter'a basınız...")
        # False geri döndüğü müddetçe
        # yukarıdaki sonsuz while döngüsünde bu fonksiyon
        # dönüp duracak.
        # True  döndüğü zaman if devreye girip döngüden çıkacak
        return False
# end of class Oyun


# Bu da oyun kurulumu
oyun = Oyun()
# 3 rakip olsun dedim
oyun.yeni(3)
# AAAAND ACTION!
oyun.baslat()
