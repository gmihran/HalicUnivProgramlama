"""
Bu bir açıklama bloğudur.
Bu satır da açıklama satırına sahildir.
"""
#Bu bir açıklama satırıdır.
#Program çalıştırıldığında açıklama satırları derlenmez. Yani çalıştırılmaz. Bu satırlar görmezden gelinir.

print("merhaba dünya")

merhaba="merhabalar"
#merhaba bir değişkendir. Bu değişkenin içerisinde merhaba string (str) değeri saklanmaktadır. 
print(merhaba)
print(type(merhaba)) #<class 'str'>
#merhaba değişkeninin tipini (değişken türünü) ekrana yazdırdık


isim=input("İsminizi giriniz..:")
print(isim)
print("Hoş geldin "+isim)
print("Hoş geldin",isim)


sayi=int(input("Sayı giriniz..:"))
#input ile alınan veriler hafızada string olarak saklanır. Bunu (sayısal) tam sayı türüne dönüştürmek için int() fonksiyonunu kullanırız.
print(sayi)
print(type(sayi))

sayi=input("Sayı giriniz..:")
sayi=int(sayi)
print(type(sayi))

sayi=eval(input("Sayı..:"))
print(sayi)
print(type(sayi))


"""
Sayı..:1
1
<class 'int'>

Sayı..:1.2
1.2
<class 'float'>

Sayı..:1,2,3
(1, 2, 3)
<class 'tuple'>

Sayı..:[1,2,3]
[1, 2, 3]
<class 'list'>

Sayı..:{1,2,3}
{1, 2, 3}
<class 'set'>

Sayı..:{1:"bir",2:"iki"}
{1: 'bir', 2: 'iki'}
<class 'dict'>

Sayı..: Gözde
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Gözde' is not defined
"""


#Lists (Listeler)
sayilar=[1,2,3,4,5]

#Tüm elemanları ekrana yazdıralım
print(sayilar)

#1.elemanı ekrana yazdıralım
print("ilk değer:",sayilar[0])
#indis değeri elemanın bulunduğu konumu temsil eder ve bu değer 0'dan başlar.

print("eleman sayısı:",len(sayilar))
#length (uzunluk) -> len fonksiyonu ile bir listenin uzunluğunu yani bu listenin içerisinde kaç tane değer olduğunu görebiliriz.

#son elemanı ekrana yazdıralım
#1.yöntem
print("son değer:",sayilar[4])

#2.yöntem
print("son değer:",sayilar[len(sayilar)-1])

print("Çok keyifli bir dersti. 01/04/2022 ")