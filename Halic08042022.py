"""
Değişken tanımlama kuralları:
*İngiliz alfabesindeki harfleri kullanıyoruz. Yani İ,ı,ş,ç,ö vb. harfler kullanmıyoruz.
*Sayıyla başlayamaz. Sadece sayıdan oluşamaz.
*Özel karakterlerden sadece alt çizgi (_) kullanılabilir.
*Programa özgü anahtar kelimeler kullanılamaz. 

"""

kelime="Haliç Üniversitesi"
print(kelime[7]) 

kelime="HaliçÜniversitesi"
print(kelime[2:7]) 

#deger=eval(input("Değer:"))
#print(type(deger))
"""
Değer:10.5
<class 'float'>
"""

print(10//3)
#Bölüm sonucunun tam kısmını alır 
#3

print(10/3)
#Bölüm sonucunu alır
#3.3333333333333335

print(10%3)
#10 mod 3 yani 10 değerinin 3'e bölümünden kalanını alır.
#1

print(10**2)
#10 değerinin 2 üssünü alır
#100

