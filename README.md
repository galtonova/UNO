# PyUNO
Python 3 ile UNO oyunu

n kadar bilgisayara karşı UNO oynatan konsol tabanlı bir python programı

    class KartTurleri:
        siyah = 0
        kirmizi = 1
        sari = 2
        yesil = 3
        mavi = 4
        pas_gec = 10
        yon_degistirici = 11
        arti2 = 12
        renk_degistirici = 13
        arti4 = 14

----

    class Kart:
        renk = 0
        deger = 0
        def __str__(self):
        def __init__(self, r, d):

---

    class Deste:
        deste = []
        def yeni_karisik_deste(self):
        def ilk_karti_cek(self):
        def kart_cek(self, n=1, yerdekiler=False):
        def ustteki(self):
        def uste_kart_koy(self, kart):
        def karistir(self):

----

    class Oyuncu:
        insan = False
        el = []
        isim = ""
        def yeni_el(self, kartlar):
        def kart_ver(self, kart: Kart):
        def oyna(self, ortadaki, ikinci=False):
    
----
    
    class Oyun:
        ana_deste = Deste()
        yerdeki_deste = Deste()
        oyuncular = []
        siradaki = -1
        yon = 1
        def yeni(self, n=3):
        def ortayi_degerlendir(self):
        def baslat(self):
        def siradaki_oyuncu(self):
    
----

-- Tolga G.


