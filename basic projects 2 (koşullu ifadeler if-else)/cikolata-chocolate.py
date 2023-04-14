# "n" ve "m" boutlarındaki bir çikolatayı düz şekilde bir kez bölmeye izin verilirse, "k" bölüme ayrılabilir mi ?

n = int(input("Bir kenarı giriniz: "))
m = int(input("Bir kenarı giriniz: "))
k = int(input("kaç parça istediğiniiz giriniz: "))

if ((n*m) > k) and ((k%n==0)or(k%m==0)):
    print("EVET")
else:
    print("HAYIR")
    
        