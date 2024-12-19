fi=open("./18-12-2024/bai3/bai3.inp","r")
fo=open("./18-12-2024/bai3/bai3.out","w")
A=[int(x) for x in fi.readline().split()]
tong=0.0
Tien_1=0
Tien_2=300000*0.2
Tien_3=300000*0.5
Tien_4=300000
Tien_5=300000*0.8
for x in A:
  if x<=5:
    tong+=Tien_1
  elif 5<=x<=10:
    tong+=Tien_2
  elif 10<=x<=15:
    tong+=Tien_3
  elif 16<x<60:
    tong+=Tien_4
  elif x>65:
    tong+=Tien_5
print(tong)  