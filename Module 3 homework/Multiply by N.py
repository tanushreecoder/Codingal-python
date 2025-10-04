def fun1(n):
  n = int(input("Enter a num"))
  return n*(n+1)/2
print(fun1(4))

def fun2(m):         
   m = int(input("Enter a num"))
   sum = 0
   for i in range(1, m+1):
       sum += i