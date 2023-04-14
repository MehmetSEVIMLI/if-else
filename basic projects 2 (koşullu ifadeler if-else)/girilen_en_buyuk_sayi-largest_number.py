# if/else kullanarak girilen 3 sayının hangisinin daha büyük olduğunu bulan fonksiyonu yazınız.

a = int(input("sayı giriniz: "))
b = int(input("sayı giriniz: "))
c = int(input("sayı giriniz: "))

if a>b and a>c:
    print("en büyük sayı: ",a)
elif b>a and b>c:
    print("en büyük sayı: ",b)
elif c>b and c>a:
    print("en büyük sayı: ",c)
else:
    print("hatalı giriş.")