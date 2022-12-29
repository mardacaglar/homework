#sinav_sonuc isimli bir sözlük oluşturdum.
sinav_sonuc={'isimler': ['Ayse K','Ahmet M','Nuri C','Nawar T','Suzan T','Ala B'],'cinsiyet': ['K','E','E','E','K','K'],'Matematik': [80,60,77,25,36,75],'Turkce': [90,50,53,100,98,66],}
count_k=0 #Kadın sayısını 0 olarak başlattım.
count_e=0 #Erkek sayısını 0 olarak başlattım.
e_mat=0 #Erkeklerin matematik notlarının toplamını 0 olarak başlattım.
k_mat=0 #Kadınların matematik notlarının toplamını 0 olarak başlattım.
t_ort=0 #Türkçe not ortalamalarını 0 olarak başlattım.
k_turkcenot=[] #Kadınların Türkçe notlarını ekleyeceğim boş bir liste yaptım.
e_turkcenot=[] #Erkeklerin Türkçe notlarını ekleyeceğim boş bir liste yaptım.
#matematik dersinin kadınlar ve erkekler için ayrı ayrı ortalamasını hesapladım.
for x in range(len (sinav_sonuc['cinsiyet'])):#listenin uzunluğunu range olarak aldım.
  if sinav_sonuc['cinsiyet'][x]=='K':#Cinsiyetin 'K'olup olamdığına baktım.
    count_k +=1 #Cinsiyet 'K'olunca kadın sayısını 1 arttırdım.
    k_mat=k_mat+sinav_sonuc['Matematik'][x] #kadınların matematik notlarının toplamını hesapladım.
  else: # Cinsiyetin 'E' olduğu duruma baktım.
    count_e +=1 #Cinsiyet 'E' olunca erkek sayısını 1 arttırdım.
    e_mat=e_mat+sinav_sonuc['Matematik'][x] #kadınların matematik notlarının toplamını hesapladım.
print(f"kadınların matematik ortalaması:",k_mat/count_k) #Kadınların  ortalamasını yazdırdım.
print(f"erkeklerin matematik ortalaması:",e_mat/count_e) #Erkeklerin  ortalamasını yazdırdım.
#Türkçe ortalamalarını hesapladım.
for x in range(len(sinav_sonuc['Turkce'])):#listenin uzunluğunu range olarak aldım.
 t_ort=t_ort+sinav_sonuc['Turkce'][x] #Türkçe ortalamalarını hesapladım.
print(f"Türkçe ortalamaları:",t_ort/(count_k+count_e)) #Türkçe ortalamalarını yazdırdım.
#kadınların en yüksek Türkçe notunu ve erkeklerin en yüksek Türkçe notunu yazdırdım.
for x in range(len (sinav_sonuc['cinsiyet'])): #listenin uzunluğunu range olarak aldım.
  if sinav_sonuc['cinsiyet'][x]=='K' :#Cinsiyetin 'K'olup olamdığına baktım.
    k_turkcenot.append(sinav_sonuc['Turkce'][x]) #listeye kadınların notlarını ekledim.
  else: #Cinsiyetin 'E' olduğu duruma baktım.
     e_turkcenot.append(sinav_sonuc['Turkce'][x]) #listeye erkeklerin notlarını ekledim.
print(f"kadinlarin max Türkçe notu:", max(k_turkcenot)) #kadınların en yüksek Türkçe notunu yazdırdım.
print(f"erkeklerin max Türkçe notu:",max(e_turkcenot)) #Erkeklerin en yüksek Türkçe notunu yazdırdım.
   


  

   
  


   



  
   
    