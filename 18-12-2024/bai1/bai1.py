fi=open("./18-12-2024/bai1/bai1.inp","r")
fo=open("./18-12-2024/bai1/bai1.out","w")
A=[int(x) for x in fi.readline().split()]
A.sort()

doan_du_1=max(A[0],A[1])-min(A[0],A[1])
doan_du_2=max(A[2],A[3])-min(A[2],A[3])

chieu_dai=max(A[0],A[1])-doan_du_1
chieu_rong=max(A[2],A[3])-doan_du_2

print(chieu_dai*chieu_rong,file=fo)
