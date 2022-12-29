kurs_kayit={ 'isim':['x','Ayse K.', 'Ahmet M.', 'Nuri C.','Nawar T.', 'Suzan T.', 'Ala B.'],
'cinsiyet': ['x','K', 'E', 'E','E','K', 'K'], 'matematik' : [0,80,60,77,25,36,75], 'turkce' :[0,90,50,53,100,98,66] }
# Kadin, erkek, kadinlarin matematik not ortalamasi, erkeklerin matematik not ortalamalari ve turkcede not ortalamasini bulmak icin sayaclar atandi.
sayac_kadin = 0
sayac_erkek=0
toplam_matematik_kadin=0
toplam_turkce_kadin=0
toplam_matematik_erkek=0
toplam_turkce_erkek=0
# "For i in range ..." komutu i sayisi ve sayacindan "..." yerine girilecek degere kadar verilen deger kadar artittirir (1'er ve kacar isterseniz.). Biz de range(ust sinir) olarak "len(kurs_kayit['isim'])" yani  sinav_sonuc kutuphanesinin 'isim' alt dalinin uzunlugunu aldim ve i sayaci atadim.
for i in range (len(kurs_kayit['isim'])):
# i'nin yalnizca 1 den buyuk esit oldugu degerleri aldim cunku 'i-1'. indeksi kullanirken 0. indekste '-1'. indeksi yani sonuncusunu alir bu da kod icin bir hatali bir deger verir.
    if i>=1:
        if kurs_kayit['cinsiyet'][i] == 'K':
# kurs_kayit['cinsiyet'][i] yani kurs kayittaki cinsiyet alt dalinda i. indeksin kadin oldugu durumlari baz aldim. Ve ayni mantik ve metodla matematik ve turkce notlarini topladim.
            sayac_kadin +=1
            toplam_matematik_kadin= toplam_matematik_kadin + kurs_kayit['matematik'][i]
            toplam_turkce_kadin = toplam_turkce_kadin + kurs_kayit['turkce'][i]
            n=1
# kadinlarin bir önceki notu n indeks önce olarak varsayarsak i-n. indeks ile i indeksinin buyukluklerini karsilastirarak maksimum deger icin kara verdirtiyoruz.
            if kurs_kayit['cinsiyet'][i]== 'K':
                if kurs_kayit['turkce'][i]-kurs_kayit['turkce'][i-n]>=0:
                    kadinlar_max_turkce = kurs_kayit['turkce'][i]
                else :
# Eger i. terim - i-1. terim islemi yapildiginda sonuc negatif ise i. terim daha buyuktur. Maksimum bulma mantigi buna gore yapilmistir.
                    kadinlar_max_turkce = kurs_kayit['turkce'][i-n]
# n önceki terim kadin degilse n, 1 arttiriliyor. Ve n her seferinde 1'e esitleniyor. Ayni islem erkekler icin de yapildi.
            else:
                n+=1
                if kurs_kayit['turkce'][i]-kurs_kayit['turkce'][i-n]>=0:
                    kadinlar_max_turkce = kurs_kayit['turkce'][i]
                else :
                    kadinlar_max_turkce = kurs_kayit['turkce'][i-n]
        else:
            n=1
            sayac_erkek+= 1
            toplam_matematik_erkek = toplam_matematik_erkek + kurs_kayit['matematik'][i]
            toplam_turkce_erkek= toplam_turkce_erkek + kurs_kayit['turkce'][i]
            if kurs_kayit['cinsiyet'][i]== 'E':
                if kurs_kayit['turkce'][i]-kurs_kayit['turkce'][i-n]>=0:
                    erkekler_max_turkce = kurs_kayit['turkce'][i]
            
                else :
                    erkekler_max_turkce= kurs_kayit['turkce'][i-n]
            else:
                n+=1
                if kurs_kayit['turkce'][i]-kurs_kayit['turkce'][i-n]>=0:
                    erkekler_max_turkce = kurs_kayit['turkce'][i]
            
                else :
                    erkekler_max_turkce= kurs_kayit['turkce'][i-n]
# Mantiga gore hesaplamalar yapilip, yazdirildi.
kadinlar_ortalama_matematik = toplam_matematik_kadin/sayac_kadin
erkekler_ortalama_matematik = toplam_matematik_erkek/sayac_erkek
ortalama_turkce_sinif = (toplam_turkce_kadin + toplam_turkce_erkek)/ ((len(kurs_kayit['matematik']))-1)
print(f"{kadinlar_ortalama_matematik} sinifinizin kadinlarinin matematik notu ortalamasidir.") 
print(f"{erkekler_ortalama_matematik} sinifinizin erkeklerinin matematik notu ortalamasidir.") 
print(f"{ortalama_turkce_sinif} sinifinizin turkce notu ortalamasidir.") 
print(f"{erkekler_max_turkce} sinifinizin erkeklerinin maksimum turkce notudur.")
print(f"{kadinlar_max_turkce} sinifinizin kadinlarinin maksimum turkce notudur.")

