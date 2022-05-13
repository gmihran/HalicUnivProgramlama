dosya=open("isimler.txt","w")
dosya.write("Gozde\nMelike\nEnes\n")

#dosya.seek(0)
dosya.write("Ahmet\n")
#dosyanın başına giderek yazma işlemi gerçekleştirirsek w kipi ile açıldığı için metnin üzerine yazar

dosya.close()


dosya=open("isimler.txt","r+")
print(dosya.read())

dosya.write("Özge\n")

print(dosya.tell()) #25
print(dosya.read()) 
#Okuma işlemi gerçekleşmedi. 
#Çünkü kursör dosyanın sonundadır.

dosya.seek(0)
print(dosya.tell()) #0
#Okuma işlemi gerçekleşti. 
#Çünkü kursör dosyanın başındadır.

print(dosya.read())

dosya.close()

dosya=open("isimler.txt","a+")

dosya.write("Ezgi\n")

dosya.seek(0)
print(dosya.read())

dosya.seek(0)
dosya.write("Erdem\n")
#dosyanın başına giderek yazma işlemi gerçekleştirirsek a+ kipi ile açıldığı için metnin üzerine yazmaz, metni dosyanın sonuna ekler

dosya.seek(0)
print(dosya.read())

#dosya.write("0")

dosya.seek(0)
print(dosya.read())

dosya.close()

#isimler.txt dosyasındaki isimlerin tek tek kaç karakterden oluştuklarını bir listede tutulsun ve bu değerleri ekrana yazdıralım

dosya=open("isimler.txt","r")

isimler=dosya.readlines()
print(isimler)

liste=[]
for isim in isimler:
  #print(isim.split("\n"))
  liste.append(isim.split("\n")[0])

print(liste)

uzunluk=[]
for i in liste:
  uzunluk.append(len(i))
print(uzunluk)

for i in range(0,len(liste)):
  print(liste[i],"-",uzunluk[i])

dosya.close()

