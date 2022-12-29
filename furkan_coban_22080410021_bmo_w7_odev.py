#kisiler isimli boş liste oluşturalım.
kisiler=[] 
#kullanıcının ekrana girdiği 3 ismi 'string'olacak şekilde ekleyelim.
kisiler.append("furkan")
kisiler.append("emirhan")
kisiler.append("enes")
#listeyi ekrana yazdıralım.
print(kisiler)
#listenin uzunluğunu ekrana yazdıralım.
uzunluk=len(kisiler)
print(uzunluk)
#listenin 2. elemanını ekrana yazdıralım.
print(kisiler[1])
#listenin son elemanını listeden silelim.
kisiler.pop(2)
#listeyi tekrar ekrana yazdıralım.
print(kisiler)