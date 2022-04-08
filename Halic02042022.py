sayi=10
print(type(sayi))
#<class 'int'>
#Tam sayılar integer değer türündedir.

sayi=10.2
print(type(sayi))
#<class 'float'>
#Ondalıklı sayoşar float değer türündedir.

sayi=[1,2,3,4,5]
print(type(sayi))
#<class 'list'>
#[] içerisinde tanımlanan değişkenler liste türündedir.

sayi=(1,2,3,4,5)
print(type(sayi))
#<class 'tuple'>
#() içerisinde tanımlanan değişkenler demet türündedir.

sayi=5
liste=[1,2,3,4]
#sayi içerisinde saklanan değeri listeye ekleyelim.
liste.append(sayi)
#listeye bir değer eklemek için append fonksiyonu kullanılır.

print(liste)
#[1, 2, 3, 4, 5]

#Bu listeye 6 değerini ekleyelim.
liste.append(6)
print(liste)
#[1, 2, 3, 4, 5, 6]

#Bu listeye kendi ismimizi ekleyelim
liste.append("Gözde")
print(liste)
#[1, 2, 3, 4, 5, 6, 'Gözde']

#Bu listeye kendi soyismimizi ekleyelim
liste.append('Altınsoy')
print(liste)
#[1, 2, 3, 4, 5, 6, 'Gözde', 'Altınsoy']

#string ifadeler (karakter kümeleri) yazılırken tırnak içerisine alınır.
#Bu tırnak işareti tek tırnak ('') veya çift tırnak ("") olabilir.
#Burada dikkat edilmesi gereken şey hangisiyle tırnağı açtıysak onunla kapatmalıyız.

#Aşağıdaki cümleyi ekrana yazdıralım
#Beykoz'un güzellikleri
print("Beykoz'un güzellikleri")
#Beykoz'un güzellikleri

#Aşağıdaki cümleyi ekrana yazdıralım
#Yazar "Beykoz çok güzel" demişti.
print('Yazar "Beykoz çok güzel" demişti.')
#Yazar "Beykoz çok güzel" demişti.

#Aşağıdaki cümleyi ekrana yazdıralım
#Beykoz'un "Hidiv Kasrı" 1907 yılında yapılmıştır.
print("Beykoz'un "+'"Hidiv Kasrı" 1907 yılında yapılmıştır.')
#Beykoz'un "Hidiv Kasrı" 1907 yılında yapılmıştır.

"""
Hesaplama İşlemleri
Toplama +
Ör: 5+2=7

Çıkarma -
Ör: 5-2=3

Çarpma *
Ör: 5*2=10

Bölme /
Ör: 5/2=2.5

Kalan (mod) %
Ör:5%2=1

Üs alma **
Ör: 5**2=25

Kalansız bölme (Tam kısmı alarak bölme) //
Ör: 5//2=3
"""
print(5//2)
#2

print(5//3)
#1

#10 ile -5 sayılarının toplamını ekrana yazdıralım
print(10+(-5))
#5

#10 ile -5 sayılarının farkını ekrana yazdıralım
print(10-(-5))
#15

#10 ile -5 sayılarının çarpımlarının sonucunu ekrana yazdıralım
print(10*-5)
#-50

#10 ile -5 sayılarının bölümlerinin sonucunu ekrana yazdıralım
print(10/-5)
#-2.0

#10 ile -4 sayılarının bölümlerinin sonucunu ekrana yazdıralım
print(10/-4)
#-2.5

#10 ile -4 sayılarının bölümlerinin sonucunun tam kısmını ekrana yazdıralım
print(10//(-4))
#-3

#10 ile 3 sayılarının bölümlerinin sonucunun tam kısmını ekrana yazdıralım
print(10//3)
#3

#10 ile 4 sayılarının bölümlerinin sonucunun tam kısmını ekrana yazdıralım
print(10//4)
#2

#10 ile 4 sayısının bölümünden kalan değeri (modunu) ekrana yazdıralım
print(10%4)
#2

#8 sayının 3 üssünü ekrana yazdıralım
print(8**3)
#512

"""
Hesap Makinesi
Kullanıcıdan iki tane sayı alalım.
Bu sayıları toplama, çıkarma,çarpma ve bölme işlemlerine tabii tutup sonuçları ekrana yazdıralım
Örnek çıktı:
1.sayıyı giriniz..:10
2.sayıyı giriniz..:5
10+5=15
10-5=5
10*5=50
10/5=2
"""
sayi1=int(input("1.sayıyı giriniz..:"))
sayi2=int(input("2.sayıyı giriniz..:"))
print(sayi1,"+",sayi2,"=",sayi1+sayi2)
print(sayi1,"-",sayi2,"=",sayi1-sayi2)
print(sayi1,"*",sayi2,"=",sayi1*sayi2)
print(sayi1,"/",sayi2,"=",sayi1/sayi2)

"""
1.sayıyı giriniz..:6
2.sayıyı giriniz..:3
6 + 3 = 9
6 - 3 = 3
6 * 3 = 18
6 / 3 = 2.0
"""

"""
1.sayıyı giriniz..:10
2.sayıyı giriniz..:0
10 + 0 = 10
10 - 0 = 10
10 * 0 = 0
Traceback (most recent call last):
  File "main.py", line 150, in <module>
    print(sayi1,"/",sayi2,"=",sayi1/sayi2)
ZeroDivisionError: division by zero
"""
#sayi2 klavyeden sıfır (0) girilirse ZeroDivisionError: division by zero hatası ortaya çıkar. Yani bölen sayı sıfır olamaz. Bu hatanın önüne geçmek için hata yakalama işlemleri yapılabilir veya koşullu ifadeler (if) ile hatanın önüne geçilebilir. İlerleyen haftalarda bu konuya bakacağız.
