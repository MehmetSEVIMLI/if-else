## iç içe koşullu ifadeler kullanarak girilen "x" ve "y" değerlerinin kordinat sisteminde kaçıncı bölgeyi gösterdiğini bulan kodu yazınız.


x=int(input("sayı giriniz: "))
y=int(input("sayı giriniz: "))

if x>0:
    if y>0:
        print("I. Bölgede bulunuyor")
    elif y<0:
        print("IV. Bölgede bulunuyor")
        
elif x<0:
    if y>0:
        print("II. Bölgede bulunuyor")
    elif y<0:
        print("III. Bölgede bulunuyor")
        
else: 
    print("hatalı giriş.")