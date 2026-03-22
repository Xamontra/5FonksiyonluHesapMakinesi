def toplama(sayilar):
    sonuc = 0
    for s in sayilar:
        sonuc += s
    return sonuc

def cikarma(sayilar):
    sonuc = sayilar[0]
    for s in sayilar[1:]:
        sonuc -= s
    return sonuc

def carpma(sayilar):
    sonuc = 1
    for s in sayilar:
        sonuc *= s
    return sonuc

def bolme(sayilar):
    sonuc = sayilar[0]
    for s in sayilar[1:]:
        sonuc /= s
    return sonuc

def karekokalma(a):
    return a ** 0.5


islem = int(input("1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n5-Karekök Alma\nSeçin: "))

sayilar_str = input("İşlem yapılmasını istediğiniz sayıları aralarında virgül olacak şekilde girin: ")
sayilar = [int(x) for x in sayilar_str.split(",")]

if islem == 1:
    print("Toplam:", toplama(sayilar))
elif islem == 2:
    print("Çıkarma:", cikarma(sayilar))
elif islem == 3:
    print("Çarpma:", carpma(sayilar))
elif islem == 4:
    print("Bölme:", bolme(sayilar))
elif islem == 5:
    print("Karekök:", karekokalma(sayilar[0]))
else:
    print("Geçersiz seçim!")