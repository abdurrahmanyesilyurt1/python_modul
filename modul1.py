def sayi_mi(karakter):
    return karakter.isdigit()

def ters_cevir(metin):
    return metin[::-1]

def sesli_harfleri_say(metin):
    sesli_harfler = 'aeıioöuüAEIİOÖUÜ'
    return sum(1 for harf in metin if harf in sesli_harfler)

def kelime_sayisi(metin):
    return len(metin.split())

def buyuk_harf_yap(metin):
    return metin.upper()

def en_uzun_kelime(metin):
    kelime_listesi = metin.split()
    return max(kelime_listesi, key=len)

def karakter_sayisi(metin):
    return len(metin)

def kucuk_harf_yap(metin):
    return metin.lower()

def kisisel_bilgileri_al():
    ad = input("Adınızı giriniz: ")
    soyad = input("Soyadınızı giriniz: ")
    ogrenci_numarasi = input("Öğrenci numaranızı giriniz: ")
    print(f"Hoşgeldiniz, {ad} {soyad}!")
    return ad, soyad, ogrenci_numarasi

def fonksiyon_secimi():
    while True:
        print("\nLütfen çalıştırmak istediğiniz fonksiyonu seçin:")
        print("1: Sayı mı kontrolü")
        print("2: Metni ters çevirme")
        print("3: Sesli harf sayımı")
        print("4: Kelime sayısı bulma")
        print("5: Metni büyük harfe çevirme")
        print("6: En uzun kelimeyi bulma")
        print("7: Karakter sayısını bulma")
        print("8: Metni küçük harfe çevirme")
        print("9: Çıkış (9 yazarak çıkabilirsiniz)")
        secim = input("Seçiminizi yapın (1-9): ")

        if secim == '9':
            print("Programdan çıkılıyor...")
            break

        elif secim == '1':
            karakter = input("Kontrol edilecek karakteri girin: ")
            print(f"'{karakter}' bir sayı mı? {sayi_mi(karakter)}")
        elif secim == '2':
            metin = input("Tersine çevrilecek metni girin: ")
            print(f"Metnin tersi: {ters_cevir(metin)}")
        elif secim == '3':
            metin = input("Sesli harf sayımı yapılacak metni girin: ")
            print(f"Metindeki sesli harf sayısı: {sesli_harfleri_say(metin)}")
        elif secim == '4':
            metin = input("Kelime sayısını bulmak için metin girin: ")
            print(f"Metindeki kelime sayısı: {kelime_sayisi(metin)}")
        elif secim == '5':
            metin = input("Büyük harfe çevrilecek metni girin: ")
            print(f"Metnin büyük harfli hali: {buyuk_harf_yap(metin)}")
        elif secim == '6':
            metin = input("En uzun kelimeyi bulmak için metin girin: ")
            print(f"Metindeki en uzun kelime: {en_uzun_kelime(metin)}")
        elif secim == '7':
            metin = input("Karakter sayısını bulmak için metin girin: ")
            print(f"Metindeki karakter sayısı: {karakter_sayisi(metin)}")
        elif secim == '8':
            metin = input("Küçük harfe çevrilecek metni girin: ")
            print(f"Metnin küçük harfli hali: {kucuk_harf_yap(metin)}")
        else:
            print("Geçersiz seçim. Lütfen verilen seçeneklerden birini girin.")

kisisel_bilgileri_al()
fonksiyon_secimi()
