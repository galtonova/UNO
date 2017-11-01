import random
import os
from time import sleep

class KartTurleri:
    # Kart Renkleri
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


class Deste:
    deste = []

    # Deste Oluştur
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
    # Ana destedeki kartlar bitince yerdeki kartlar destesi
    # karıştırılıp kullanılacak

    def ustteki(self):
        return self.deste[0]

    def uste_kart_koy(self, kart):
        self.deste.insert(0, kart)

    def karistir(self):
        random.shuffle(self.deste)

    # --------------------------

    def __str__(self):
        t = "{\n"
        for index, k in enumerate(self.deste):
            t += "\t{" + str(index).zfill(3) + ": " + str(k) + " },\n"
        t += "}"
        return t
# end of class Deste


class Oyuncu:
    insan = False
    el = []
    isim = ""

    def yeni_el(self, kartlar):
        self.el = kartlar

    def kart_ver(self,kart: Kart):
        self.el.append(kart)

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
                    print(" 0. Pas Geç")
                for i, kart in enumerate(self.el):
                    if ortadaki.renk == kart.renk or ortadaki.deger == kart.deger or kart.renk == KartTurleri.siyah:
                        if i + 1 >= 10:
                            print(str(i + 1) + ". " + str(kart))
                        else:
                            print(" "+str(i + 1) + ". " + str(kart))
                    else:
                        print("    " + str(kart))
                secim = int(input("Kart No: "))-1
            else:
                secilebilecekler = []
                jokerler = []
                for k in range( len(self.el) ):
                    kart = self.el[k]
                    if ortadaki.renk == kart.renk or ortadaki.deger == kart.deger:
                        secilebilecekler.append(k)
                    elif kart.renk == KartTurleri.siyah:
                        jokerler.append(k)
                if len(secilebilecekler) > 0:
                    secim = secilebilecekler[random.randint(0,len(secilebilecekler)-1)]
                elif len(jokerler) > 0:
                    secim = jokerler[random.randint(0, len(jokerler) - 1)]
                else:
                    secim = -1

            secilen = self.el[secim]

            if secilen.renk == KartTurleri.siyah:
                renk = ""
                if self.insan:
                    renk = input("Yeni Renk: ")
                else:
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

                if renk[0].lower() == "m":
                    renk = KartTurleri.mavi
                elif renk[0].lower() == "s":
                    renk = KartTurleri.sari
                elif renk[0].lower() == "y":
                    renk = KartTurleri.yesil
                elif renk[0].lower() == "k":
                    renk = KartTurleri.kirmizi

                del self.el[secim]
                return Kart(renk, secilen.deger)

            elif ortadaki.renk == secilen.renk or ortadaki.deger == secilen.deger:
                del self.el[secim]
                return secilen
            elif secim == -1:
                return -1
    # end of def oyna
# end of class oyuncu


class Oyun:
    ana_deste = Deste()
    yerdeki_deste = Deste()
    oyuncular = []
    siradaki = -1
    yon = 1

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

    def ortayi_degerlendir(self):
        ortadaki = self.yerdeki_deste.ustteki()
        # pas_gec
        # yon_degistirici
        # arti2
        # renk_degistirici
        # arti4
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

    def baslat(self):
        print("YENİ OYUN BAŞLADI")
        print("---------------------------")
        print(self.yerdeki_deste.ustteki())
        print("---------------------------")
        self.ortayi_degerlendir()
        self.siradaki += self.yon
        input("Devam etmek için Enter'a basınız...")
        while True:
            if self.siradaki_oyuncu():
                break

    def siradaki_oyuncu(self):
        self.siradaki = self.siradaki % len(self.oyuncular)
        if self.oyuncular[self.siradaki].insan:
            os.system('cls' if os.name == 'nt' else 'clear')
        print("---------------------------")
        print("deste:", str(len(self.ana_deste.deste)), end='')
        for o in range(len(self.oyuncular)):
            print(" o", str(o), ":", str(len(self.oyuncular[o].el)), sep='', end='')
        print("\n---------------------------")
        kart = self.oyuncular[self.siradaki].oyna(self.yerdeki_deste.ustteki())
        if kart == -1:
            # oyuncu kart çekmek istiyor
            sleep(0.5)
            print(self.oyuncular[self.siradaki].isim, "Kart Çekti")
            self.oyuncular[self.siradaki].kart_ver(self.ana_deste.kart_cek(1,self.yerdeki_deste))
            kart = self.oyuncular[self.siradaki].oyna(self.yerdeki_deste.ustteki(),True)
        if kart == -1:
            # oyuncu kart atmadı
            print(self.oyuncular[self.siradaki].isim,"Kart Atmadı")
        else:
            # oyuncu kart attı
            print(self.oyuncular[self.siradaki].isim,"Kart Attı")
            print("Atılan Kart:",kart)
            self.yerdeki_deste.uste_kart_koy(kart)

            if len(self.oyuncular[self.siradaki].el) == 0:
                print("---------------------------")
                print(self.oyuncular[self.siradaki].isim," KAZANDI!")
                print("---------------------------")
                return True
            elif len(self.oyuncular[self.siradaki].el) == 1:
                print("---------------------------")
                print(self.oyuncular[self.siradaki].isim, " UNO!")
                print("---------------------------")
            self.ortayi_degerlendir()
        self.siradaki += self.yon
        input("Devam etmek için Enter'a basınız...")
        return False
# end of class Oyun


oyun = Oyun()
oyun.yeni(3)
oyun.baslat()
i = 5
