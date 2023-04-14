# Girilen a,b,c sayıalrı üçgen olşturur mu? oluşturuyorsa program Evet, değilse Hayır yazacak.

# bir şeklin üçgen olabilmesi için herhangi iki kenarın toplmaı diğer kenardan büyük olmalıdır.


a=int(input("Uzunluk giriniz: "))
b=int(input("Uzunluk giriniz: "))
c=int(input("Uzunluk giriniz: "))


if ((a+b)>c) and ((a+c)>b) and ((c+b)>a):
    print("EVET")
else: 
    print("HAYIR")