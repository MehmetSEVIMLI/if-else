# girilen yıl artık yıl ise EVET, değilse HAYIR yazan programı yazınız.

#artık yıl, miladi takvimde 365 yerine 366 günü olan yıldır.
# Eğer yıl 400'ün katı ise artık yıldır. Veya 4'ün katı ama 100'ün katı değilse yine artık yıldır.
year = int(input("Yıl giriniz: "))

if (year%400==0) or ((year%4 ==0) and (year%100!=0)):
    print("EVET")
else:
    print("HAYIR")