#Matematik Oyunu
#1 ile 100 arasında 2 tam sayı üretip, rastgele +,-,* işlemlerinden birini seçip sonucu kullanıcıdan isteyelim.
#Kullanıcı doğru cevap verirse 1 puan kazansın. Ekrana kullanıcının aldığı puan yazdırılsın.

import random

#import bir modülü(kütüphaneyi) projemize dahil etmemizi sağlar.
#Soru: Bir modülü(kütüphaneyi) projemize dahil etmemizi sağlayan kod yapısı aşağıdakilerden hangisidir?
#Cevap: import

#random rastgele bir değer üretmek için kullanılan bir modüller.
#Soru: Rastgele bir değer üretmek için kullanılan  modül aşağıdakilerden hangisidir?
#Cevap: random

#print(random.randint(1,3))
#1 ile 3 arasında (1 ve 3 dahil) bir sayı üretir

puan=0

x=random.randint(1,100)
#1-100 arasında rastgele bir değer üretip bunu x değişkeninde saklıyoruz.

y=random.randint(1,100)
#1-100 arasında rastgele bir değer üretip bunu y değişkeninde saklıyoruz.

islemler=["+","-","*"]
islem=random.choice(islemler)
#islemler listesinden rastgele bir değer seçiyoruz. Bu değeri islem değişkeninde saklıyoruz.
if islem=="+":
  sonuc=x+y #sonuc değişkeninin türü integer'dır
  print(x,"+",y,"=",end=" ")
  tahmin=int(input(""))
elif islem=="-":
  sonuc=x-y 
  print(x,"-",y,"=",end=" ")
  tahmin=int(input(""))
else:
  sonuc=x*y 
  print(x,"*",y,"=",end=" ")
  tahmin=int(input(""))
  
if sonuc==tahmin:
  puan=puan+1
  print("Doğru Tahmin")
else:
  print("Yanlış Tahmin. Sonuç:",sonuc)

print("Puanınız:",puan)



sorucevap={"Türkiye'nin başkenti neresidir?":"Ankara","Kardeşimin Hikayesi kitabının yazarı kimdir?":"Zülfü Livaneli","Osmanlının kurucusu kimdir?":"Osman Bey","Türkiyenin en yüksek dağı?":"Ağrı Dağı","Dünyanın en büyük dağı?":"Everest","Atatürk'ün doğum tarihi?":"1881"} 

puan=0

print(len(sorucevap)) 

for soru,dogrucevap in sorucevap.items():
  cevap=input(soru)
  if dogrucevap.capitalize()==cevap.capitalize():
    print("Doğru cevap")
    puan=puan+1
  else:
    print("Yanlış cevap")

print("Puanınız:",puan)