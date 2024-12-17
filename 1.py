fi=open("D:\\longn\\BÀI TẬP\\9.11.2024\\1.inp","r")
fo=open("D:\\longn\\BÀI TẬP\\9.11.2024\\1.out","r")
a=int(fi.readline())
def dragon(n):
  if n==0:
    return 0
  else:
    return n**2 + dragon(n-1)
print(dragon(a))