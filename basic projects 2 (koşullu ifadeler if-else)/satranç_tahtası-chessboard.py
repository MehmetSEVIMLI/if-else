# satranç tahtası üzerinde x ve y koordinatları ile 2 nokta veriliyor.
# bu iki nokta aynı renkte ise "AYNI" değilse "FARKLI" yazan progarmı yazınız.
# programa 4 sayı giriliyor. 1.ve 2. sayılar birinci nokta, 2. ve 4. sayılar ikinci noktanın koordinatları.


a=int(input("1. sayı: "))
b=int(input("2. sayı: "))
c=int(input("3. sayı: "))
d=int(input("4. sayı: "))

x=a+b
y=c+d

if x%2==0:
    if y%2==0:
        print("renkler 'AYNI' ")
else:
    print("Renkler 'FARKLI' ")    