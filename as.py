str ="I love you"
A = list(str)
c =A[0]
A[0]=A[-1]
A[-1]=c
s=''
a=s.join(A)
print(a)
