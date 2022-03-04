def hizalama(kelimeler,satir_genisligi):
    ilk_kelime = 0
    kelime_sayisi = 0
    satir_kelime_karakter_toplami = 0
    hizali_metin = []
    for i in range(len(kelimeler)):
        if satir_kelime_karakter_toplami + kelime_sayisi + len(kelimeler[i]) > satir_genisligi:
            bir_satir = []
            if kelime_sayisi > 1:
                bosluk = (satir_genisligi - satir_kelime_karakter_toplami) // (kelime_sayisi - 1)
                ek_bosluk = (satir_genisligi - satir_kelime_karakter_toplami) % (kelime_sayisi - 1)
            for j in range(ilk_kelime, i):
                bir_satir.append(kelimeler[j])
                if j == i - 1:
                    break
                for n in range(0, bosluk):
                    bir_satir.append(' ')
                if j - ilk_kelime < ek_bosluk:
                    bir_satir.append(' ')
            if kelime_sayisi == 1:
                for n in range(len(kelimeler[ilk_kelime]), satir_genisligi):
                    bir_satir.append(' ')
            hizali_metin.append(''.join(bir_satir))
            ilk_kelime = i
            kelime_sayisi = 0
            satir_kelime_karakter_toplami = 0
        kelime_sayisi += 1
        satir_kelime_karakter_toplami += len(kelimeler[i])
    bir_satir = []
    if ilk_kelime == 0 or ilk_kelime < len(kelimeler):
        bir_satir = []
        for j in range(ilk_kelime, len(kelimeler)):
            bir_satir.append(kelimeler[j])
            if j == len(kelimeler) - 1:
                break
            bir_satir.append(' ')
        for n in range(len(''.join(bir_satir)), satir_genisligi):
            bir_satir.append(' ')
        hizali_metin.append(''.join(bir_satir))
    for i in range(len(hizali_metin)):
        print(hizali_metin[i])
    return hizali_metin
def kelime_say(kelime_tekrarlari,kelimeler): # kelimenin kaç kere tekrar ettiğini bulduğumuz fonksiyon
    for x in kelimeler: # metindeki tüm kelimeleri içeren ve onları sayan sözlüğümüzü oluşturacak döngü.
        try:
            kelime_tekrarlari[x] += 1
        except:
            kelime_tekrarlari[x] = 1

    return kelime_tekrarlari

import locale  # alfabetik şekilde yazdırabilmek için
locale.setlocale(locale.LC_ALL, "tr_TR.utf8")
import operator # sözlüğü değerlerinin büyüklüklerine göre sıralamak için kullanacağımız kütüphane

tum_kelimeler = []
devam = "e"
while devam.upper() == "E":
    metin = input("Metninizi giriniz : ")
    metin = metin.replace("i","İ").upper()
    kelimeler = metin.split() # kelimelerin listesi oluşturuldu.
    kelime_tekrarlari = {} # metindeki kelimeleri saymak için
    kelime_say(kelime_tekrarlari,kelimeler)
    satir_genisligi = int(input("Metninizi hizalamak istediğiniz satır genişliğini giriniz : "))
    while satir_genisligi != 0:
        hizalama(kelimeler, satir_genisligi)
        satir_genisligi = int(input("Metninizi hizalamak istediğiniz  başka bir satır genişliğini girebilirsiniz : "))
    kelime_listesi = []
    for key in kelime_tekrarlari:
        kelime_listesi.append(key)
    alfabetik_sirali_liste = sorted(kelime_listesi,key=locale.strxfrm) # kelime listemizi alfabetik sıraya koyarak yeni bir listeye atadık
    for x in range(len(kelimeler)):
        tum_kelimeler.append(kelimeler[x])

    deger_buyukluk_sirali_liste = sorted(kelime_tekrarlari.items(),key=operator.itemgetter(1),reverse=True)# değer büyüklüğüne göre yazdıracağımız print için listeyi olşuutrduık.

    #for x in range(len(deger_buyukluk_sirali_liste)):   # oluşan sıralı listemizin içindeki tuple ları listeye dönüştürdük ki iç içe liste ile ekrana yazdırabilelim
    #    deger_buyukluk_sirali_liste[x] = list(deger_buyukluk_sirali_liste[x])
    print("Kelime              Tekrar Say     |     Kelime              Tekrar Say")
    print("------------------- ----------     |     ------------------- ----------")
    for x in range(len(kelime_listesi)):
        print(format(alfabetik_sirali_liste[x],"<23"),end=" ")
        print(format(kelime_tekrarlari[alfabetik_sirali_liste[x]],"<5"),end="      |      ")
        print(format(deger_buyukluk_sirali_liste[x][0],"<23"),end=" ")
        print(format(deger_buyukluk_sirali_liste[x][1],"<5"))
    devam = input("Başka bir metin girmek istiyor musunuz ? ")
print("")
tum_kelime_tekrarlari = {}
kelime_say(tum_kelime_tekrarlari,tum_kelimeler)
tum_tek_kelimeler = []
for key in tum_kelime_tekrarlari:
    tum_tek_kelimeler.append(key)
alfabetik_tum_kelimeler = sorted(tum_tek_kelimeler,key=locale.strxfrm)
tum_degerler_sirali_liste = sorted(tum_kelime_tekrarlari.items(),key=operator.itemgetter(1),reverse=True)

print("Kelime              Tekrar Say     |     Kelime              Tekrar Say")
print("------------------- ----------     |     ------------------- ----------")
for x in range(len(tum_tek_kelimeler)):
    print(format(alfabetik_tum_kelimeler[x], "<23"), end=" ")
    print(format(tum_kelime_tekrarlari[alfabetik_tum_kelimeler[x]], "<5"), end="      |      ")
    print(format(tum_degerler_sirali_liste[x][0], "<23"), end=" ")
    print(format(tum_degerler_sirali_liste[x][1], "<5"))

alfabe = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
harf_tablosu = []
for x in range(len(alfabe)):
    harf_tablosu.append([0]*20)
for x in range(len(tum_kelimeler)):
    for y in range(len(alfabe)):
        index = tum_kelimeler[x].find(alfabe[y])
        while index != -1:
            harf_tablosu[y][index] += 1
            index = tum_kelimeler[x].find(alfabe[y],index+1)
print("")

def index_tablosu():
    print("Harf",end= "   ")
    for x in range(20):
         print(format(x+1,"<3"),end=" ")
    print("Toplam")
    print("----",end="  ")
    for x in range(20):
        print("---",end=" ")
    print(" -------")
    for x in range(len(alfabe)):
        print(alfabe[x],end="      ")
        for y in range(20):
            print(harf_tablosu[x][y],end="")
            print("   ",end="")
        print("   ",end="")
        print(format(sum(harf_tablosu[x]), "<3"))
index_tablosu()

print("")

def uzayda_kelime_ara():
    dosya = open("harf_uzayi.txt",encoding="utf8")
    satirlar = ""
    for a in dosya.read():
        satirlar += a

    satir_uzunlugu = satirlar.index('\n') + 1  #indexler 0'dan başladığı için +1 koyduk.

    karakterler = [(harf, divmod(index, satir_uzunlugu))
                  for index, harf in enumerate(satirlar)]


    kelime_satirlari = {}
    yonler = {"GÜNEY": 0, "GÜNEY BATI": -1, "GÜNEY DOĞU": 1}  # Kelimelerin yönlerini bulmak için oluşturduğumuz algoritma:

    for kelime_yonu, yonler in yonler.items():
        kelime_satirlari[kelime_yonu] = []
        for a in range(satir_uzunlugu):
            for b in range(a, len(karakterler), satir_uzunlugu + yonler):
                kelime_satirlari[kelime_yonu].append(karakterler[b])
            kelime_satirlari[kelime_yonu].append('\n')

    # Ters yönde arama yapmak için listeler oluşturduk
    kelime_satirlari["DOĞU"] = karakterler

    bati_yonunde_karakterler = [] # bati yonunda karakter listesi olşuturacağız.
    for x in reversed(karakterler):
        bati_yonunde_karakterler.append(x)
    kelime_satirlari["BATI"] = bati_yonunde_karakterler

    guney_yonunde_karakterler = [] # guney yonunde karakter listesi oluşturacağız.
    for x in reversed(kelime_satirlari["GÜNEY"]):
        guney_yonunde_karakterler.append(x)
    kelime_satirlari["KUZEY"] = guney_yonunde_karakterler

    sag_capraz_karakterler = [] # sağ çapraz doğrultusu karakter listesi oluşturacağız.
    for x in reversed(kelime_satirlari["GÜNEY DOĞU"]):
        sag_capraz_karakterler.append(x)
    kelime_satirlari["KUZEY BATI"] = sag_capraz_karakterler

    sol_capraz_karakterler = [] # sol çapraz doğrultusu karakter listesi oluşturacağız.
    for x in reversed(kelime_satirlari["GÜNEY BATI"]):
        sol_capraz_karakterler.append(x)
    kelime_satirlari["KUZEY DOĞU"] = sol_capraz_karakterler

    def cikti(yon, tuple, satirlar):
        print("Kelime              Satır No  Sütun No  Yönü")
        print("------------------- --------  --------  ----------")

        for yon, tuple in satirlar.items():
            string = ''.join([x[0] for x in tuple])
            for kelime in tum_kelimeler:
                if kelime in string:
                    bulunan_yer = tuple[string.index(kelime)][1]
                    print(format(kelime,"<21"), format(bulunan_yer[0] + 1,"<10"),format(bulunan_yer[1] + 1,"<6"), yon)

    cikti(kelime_yonu, tuple, kelime_satirlari)

    dosya.close()

uzayda_kelime_ara()