import random

def kullanici_islem(renk, rakam):
    global deste, userdestesi, orta

    if rakam == "+2":
        userdestesi.append(deste[0])
        del deste[0]
        userdestesi.append(deste[0])
        del deste[0]
        orta = renk + " +0"
        return
    if rakam == "+4":
        userdestesi.append(deste[0])
        print(deste[0])
        del deste[0]
        userdestesi.append(deste[0])
        print(deste[0])
        del deste[0]
        userdestesi.append(deste[0])
        print(deste[0])
        del deste[0]
        userdestesi.append(deste[0])
        print(deste[0])
        del deste[0]
        orta = renk + " +0"
        return

    while True:
        print("0. Kart Çek")
        for i in range(len(userdestesi)):
            print(i+1, ".", userdestesi[i])

        buffer = int(input("Kart No = "))
        if buffer == 0:
            userdestesi.append(deste[0])
            del deste[0]
            return
        elif buffer <= len(userdestesi):
            krenk, krakam = userdestesi[buffer-1].split(" ");
            if krakam == "Değiştirici":
                renk = input("Renk Seçiniz = ")
                orta = renk + " Değiştirici"
                del userdestesi[buffer - 1]
                return
            elif renk == krenk or rakam == krakam:
                orta = userdestesi[buffer-1]
                del userdestesi[buffer-1]
                return
            elif krenk == "Renksiz":
                renk = input("Renk Seçiniz = ")
                orta = renk + " +4"
                del userdestesi[buffer - 1]
                return
#end of def kullanici_islem
def pc_islem(renk, rakam):
    global deste, pcdestesi, orta

    if rakam == "+2":
        pcdestesi.append(deste[0])
        del deste[0]
        pcdestesi.append(deste[0])
        del deste[0]
        orta = renk + " +0"
        return
    if rakam == "+4":
        pcdestesi.append(deste[0])
        print(deste[0])
        del deste[0]
        pcdestesi.append(deste[0])
        print(deste[0])
        del deste[0]
        pcdestesi.append(deste[0])
        print(deste[0])
        del deste[0]
        pcdestesi.append(deste[0])
        print(deste[0])
        del deste[0]
        orta = renk + " +0"
        return

    for buffer in range(len(pcdestesi)):
        krenk, krakam = pcdestesi[buffer].split(" ");
        if krakam == "Değiştirici":
            renk = "Mavi"
            orta = renk + " Değiştirici"
            del pcdestesi[buffer]
            return
        elif renk == krenk or rakam == krakam:
            orta = pcdestesi[buffer]
            del pcdestesi[buffer]
            return
        elif krenk == "Renksiz":
            renk = "Yeşil"
            orta = renk + " +4"
            del pcdestesi[buffer]
            return
    pcdestesi.append(deste[0])
    del deste[0]
    print("Pc kartı çekti")


deste = []
for i in range(10):
    deste.append("Kırmızı " + str(i))
    deste.append("Sarı " + str(i))
    deste.append("Mavi " + str(i))
    deste.append("Yeşil " + str(i))

for i in range(2):
    deste.append("Kırmızı +2")
    deste.append("Sarı +2")
    deste.append("Mavi +2")
    deste.append("Yeşil +2")
    deste.append("Renksiz +4")

for i in range(4):
    deste.append("Renk Değiştirici")

# deneydestesi = deste

for i in range(len(deste)):
    araveri = deste[i]
    rsayi = random.randint(0, len(deste) - 1)
    deste[i] = deste[rsayi]
    deste[rsayi] = araveri
print(deste)
print(len(deste))
"""
Burasının amacı yukarı yapılan karıştırmanın doğruğunu bulma

bulundu=0
for i in range(len(deste)):

    araveri = str(deste)
    if araveri.find(deneydestesi[i]) > -1 :
        bulundu += 1

print(bulundu)"""

userdestesi = []
pcdestesi = []
for i in range(7):
    userdestesi.append(deste[i])
    del deste[i]

    pcdestesi.append(deste[i])
    del deste[i]

orta = (deste[0])
del deste[0]
renk, rakam = orta.split(" ")
while rakam == "Değiştirici" or rakam =="+4" or rakam =="+2":
    deste.append(orta)
    orta = (deste[0])
    del deste[0]
    renk, rakam = orta.split(" ")
    print("Joker geldi")





while True:
    print("Kullanıcı = ", userdestesi)
    print("PC        = ", pcdestesi)
    renk, rakam = orta.split(" ")
    print("--------------------------")
    print(renk, rakam)
    print("--------------------------")
    kullanici_islem(renk, rakam)
    if len(userdestesi) == 0:
        print("İnsanlar kazandı")
        break
    print("Kullanıcı = ", userdestesi)
    print("PC        = ", pcdestesi)
    renk, rakam = orta.split(" ")
    print("--------------------------")
    print(renk, rakam)
    print("--------------------------")
    pc_islem(renk,rakam)
    if len(pcdestesi) == 0:
        print("Machine always wins")
        break