#Kütüphane tanımlandı.
sinav_sonuc = {'isim':['Ayse K.', 'Ahmet M.', 'Nuri C.','Nawar T.', 'Suzan T.', 'Ala B.'],   'cinsiyet': ['K', 'E', 'E','E','K', 'K'],   'vize': [80,60,77,25,36,75],  'final':[90,50,53,100,98,66] } 
#Sonradan eklenecek ogrenci sayısını istege bağlı degistirmek isteyip istemediğinizi sorguladım.
sorgu1=str(input("Girilen ogrenci sayisini kendiniz belirlemek ister misiniz?(evet ya da hayır)"))
#Yalnızca evet ya da hayır cevabını alacak şekilde bir kod yazıldı. Farklı bir cevap girmeniz halinde sorguyu tekrarlattım.
while(sorgu1 == 'evet' or 'hayır'):
    if sorgu1=='evet':
        a=int(input("girmek istediginiz ogrenci sayisini giriniz:"))
        break
    elif sorgu1=='hayır' :
        a=2
        break
    while(sorgu1!= 'evet'or 'hayır'):
       
        sorgu1= str(input("Gecersiz bir cevap yazdiniz lütfen tekrar giriniz !\n"))
        if sorgu1 == 'evet' or 'hayir':
            break
# Kullanıcıdan akınan veya odevde belirtilen ogrenci sayısına göre listeye eleman ekleyecek fonksiyon tanımlandı.
def bilgi_isleme(a):
#istege alınan kullanıcı sayısı a olarak tanımlandı ve for dongusunde kullanılması durumunda a'yı range'in son elemanı dahil ed,lmeyeceği için a'yı 1 arttırarak a'yı da dahil ettim.
    a+=1
#Tanımlama esnasında sorulacak soruların daha estetik durması için endeksleri için kullanılmak üzere bir kutuphane daha kullanıldı. İ sayısı kullanılırken bu kutuphanenin i. endeksine göre metin girilecek.
    sinif = {'bilgiler': ['isim', 'cinsiyet', 'vize','final']}    
    for i in range (1,a): 
#Range olarak 2. kurulan kutuphane kullanıldı ve k sayacı kullanıldı. K ile belirlenen indeksi sinif_sonuc kutuphanesindeki k. indeksi olan alt dala eklendi.
        for k in range(len(sinif['bilgiler'])):
            if k==2 or k==3:
                sinif1 =int(input(f"{i}.ogrenci icin {sinif['bilgiler'][k]} notunu giriniz.\n")) 
                if k==2:
                    sinav_sonuc['vize'].append(sinif1)
                if k==3:
                    sinav_sonuc['final'].append(sinif1)
            if k==1:
#k veya e ile belirtilen cinsiyetin eğer küçük harfle yazıldıysa büyütüldü.
                    sinif1 =(input(f"{i}.ogrenci icin {sinif['bilgiler'][k]}  giriniz. (k ya da e ile belirtiniz.) \n"))
                    if sinif1=='k':
                        sinif1='K'
                        sinav_sonuc['cinsiyet'].append(sinif1)
                    if sinif1== 'e':
                        sinif1='E'
                        sinav_sonuc['cinsiyet'].append(sinif1)
                    else:
                        sinav_sonuc['cinsiyet'].append(sinif1)

            elif k==0:
                sinif1 =(input(f"{i}.ogrenci icin {sinif['bilgiler'][k]}  giriniz.\n"))   
                sinav_sonuc['isim'].append(sinif1)        
# Not hesaplama için bir fonksiyon tanımlandı.
def not_hesaplama():
# Not hesaplamada hesaplanan notları eklemek için sinif_sonuc kutuphanesine ayrı bir alt dal oluşturuldu. Ve hesaplamalar yazpılarak eklendi.
    sinav_sonuc['not_ortalama']=[]
    for n in range (len(sinav_sonuc['vize'])):
        not_ortalama_ogrenci= int(0.3*sinav_sonuc['vize'][n]+ 0.7*sinav_sonuc['final'][n])
        sinav_sonuc['not_ortalama'].append(not_ortalama_ogrenci)
bilgi_isleme(a)
not_hesaplama()

print(sinav_sonuc)