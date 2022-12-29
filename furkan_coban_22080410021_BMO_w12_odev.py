#sinav_sonuc isimli bir sözlük oluşturdum.
sinav_sonuc={'isimler':['Ayse K','Ahmet M','Nuri C','Nawar T','Suzan T','Ala B'],'cinsiyet':['K','E','E','E','K','K'],'vize':[80,60,77,25,36,75],'final':[90,50,53,100,98,66],}
def Tablo():#Tablo isimli bir fonksiyon oluşturdum.
 GecmeNotu=[]#GecmeNotu isimli boş bir liste oluşturdum.
 for x in range(len(sinav_sonuc['isimler'])):#listenin uzunluğunu range olarak aldım.
   vize=sinav_sonuc['vize'][x]#vize notunu sinav_sonuc sözlüğünün vize listesinden aldım. 
   vize=float(vize)*(30/100)#vize notunun %30'unu alarak hesapladım.(vizeyi burada float değer olarak aldım.)
   final=sinav_sonuc['final'][x]#final notunu sinav_sonuc sözlüğünün final listesinden aldım.
   final=float(final)*(70/100)#final notunun %70'ini alarak hesapladım.(finali burada float değer olarak aldım.)
   gecmenotu=vize+final#gecmenotunu hesapladım.
   GecmeNotu.append(gecmenotu)#gecmenotunu GecmeNotu isimli listeye ekledim.
   sinav_sonuc.update({'GecmeNotu':GecmeNotu})#sinav_sonuc sözlüğüne GecmeNotu isimli bir satır ekledim.
Tablo()#Tablo isimli fonksiyonu çağırdım.
print("2 yeni kayıt giriniz")#kullanıcıdan 2 tane yeni kayıt girmesini istedim.
def gecmeNotu():#gecmeNotu isimli bir fonksiyon oluşturdum.
 for x in range(2):# 2 defa dönecek döngü kurdum.
   isim=input("ogrencinin ismi:")#kullanıcıdan öğrencinin ismini girmesini istedim.
   cinsiyet=input("ogrencinin cinsiyeti:")#kullanıcıdan öğrencinin cinsiyetini girmesini istedim.
   vize=float(input("ogrencinin vize notu:"))#kullanıcıdan öğrencinin vize notunu girmesini istedim.(vizeyi burada float değer olarak aldım.)
   final=float(input("ogrencinin final notu:"))#kullanıcıdan öğrencinin final notunu girmesini istedim.(finali burada float değer olarak aldım.)
   sinav_sonuc['isimler'].append(isim)#sinav_sonuc isimli sözlüğün isimler listesine kullanıcının girdiği ismi ekledim.
   sinav_sonuc['cinsiyet'].append(cinsiyet)#sinav_sonuc isimli sözlüğün cinsiyet listesine kullanıcının girdiği cinsiyeti ekledim.
   sinav_sonuc['vize'].append(vize)#sinav_sonuc isimli sözlüğün vize listesine kullanıcının girdiği vize notunu ekledim.
   sinav_sonuc['final'].append(final)#sinav_sonuc isimli sözlüğün final listesine kullanıcının girdiği final notunu ekledim.
   vize=vize*(30/100)#vize notunun %30'unu alarak hesapladım.
   final=final*(70/100)#final notunun %70'ini alarak hesapladım.
   gecmenotu=vize+final#gecmenotunu hesapladım.
   sinav_sonuc['GecmeNotu'].append(gecmenotu)#sinav_sonuc isimli sözlüğün GecmeNotu listesine gecmenotunu ekledim.
 print(sinav_sonuc)#sinav_sonuc isimli sözlüğü ekrana yazdırdım.
gecmeNotu()#gecmeNotu isimli fonksiyonu çağırdım.




 