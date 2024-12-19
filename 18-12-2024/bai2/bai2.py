fi=open("./18-12-2024/bai2/bai2.inp","r")
fo=open("./18-12-2024/bai2/bai2.inp","w")
A=[str(x) for x in fi.readline().strip()]
B=int(fi.read())

day=[]
gtri_ht=0
gtri_trc=0

for x in A:
  if x.isdigit():
    day.append(x)


day.sort()
print(''.join(day[-B:]),file=fo)





     



