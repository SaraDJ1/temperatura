dani=0
T1=int(input("Unesite temperaturu prvog dana"))
T2=int(input("Unesite temperaturu drugog dana"))
T3=int(input("Unesite temperaturu treceg dana"))
T4=int(input("Unesite temperaturu cetvrtog dana"))
prosekTemperature=(T1+T2+T3+T4)/4
if(T1<prosekTemperature):
   dani=dani+1
if(T2<prosekTemperature):
   dani=dani+1
if(T3<prosekTemperature):
   dani=dani+1
if(T4<prosekTemperature):
   dani=dani+1
print("Prosek temperature je:",prosekTemperature)
print("Ukupno dana koliko ima ispod proseka:",dani)