# Below code adds fibonacci numbers to a string
# String = abcde
# Fibonacci no of string lenght = 1 1 2 3 5
# Sum of fibonacci numbers = 12
# Expected output = 12a1b1c2d3e5

str1="abcde"
n=len(str1)
a=0
b=1
fibsum=0
ar=[1]
for i in range(1,n):
    c=a+b
    ar.append(c)
    a=b
    b=c
    fibsum+=c
k=0
str2,str3="",""
for x in str1:
    str2=x+str(ar[k])
    str3+=str2
    k+=1
str1=str(fibsum+1)+str3
print(str1)
