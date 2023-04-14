# üç basamaklı sayının basamakları toplamı çift mi yoksa tek  mi olduğunu bulan programı yazınız.

sayi = int(input("sayı giriniz: "))

ilkBasamak= sayi//100
ikinciBasamak=sayi//10%10
ucuncuBasamak = sayi%10

basamaklar_toplami=(ilkBasamak + ikinciBasamak + ucuncuBasamak)

if basamaklar_toplami%2==0:
    print("basamaklar toplamı çift.")
else: 
    print("basamaklar toplamı tek.")
