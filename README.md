# PyUNO
Python 3 ile UNO oyunu

n kadar bilgisayara karşı UNO oynatan konsol tabanlı bir python programı

    class KartTurleri:
        siyah            = 0
        kirmizi          = 1
        sari             = 2
        yesil            = 3
        mavi             = 4
        pas_gec          = 10
        yon_degistirici  = 11
        arti2            = 12
        renk_degistirici = 13
        arti4            = 14

----

    class Kart:
        renk = 0
        deger = 0
        
        def __str__()
        def __init__(r, d)

---

    class Deste:
        deste = []
        
        def yeni_karisik_deste()
        def ilk_karti_cek()
        def kart_cek(n=1, yerdekiler=False)
        def ustteki()
        def uste_kart_koy(kart)
        def karistir()

----

    class Oyuncu:
        insan = False
        el = []
        isim = ""
        
        def yeni_el(kartlar)
        def kart_ver(kart: Kart)
        def oyna(ortadaki, ikinci=False)
    
----
    
    class Oyun:
        ana_deste = Deste()
        yerdeki_deste = Deste()
        oyuncular = []
        siradaki = -1
        yon = 1
        
        def yeni(n=3)
        def ortayi_degerlendir()
        def baslat()
        def siradaki_oyuncu()
    
----

-- Tolga G.


