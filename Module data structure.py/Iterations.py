#Do the basic asymptomatic analysis for the functions written in the previous activity.

#For finding some of n natural numbers.

def fun1(n):
  return n*(n+1)/2
print(fun1(4))
                          #This uses a direct mathamatical formula. Number of steps used = 1 (Multiply, add and divide). Time complexity = O(1). Space complity = O(1)
def fun2(n):         
   sum = 0
   for i in range(1, n+1):
       sum += i
                           #In this, loop is used, if n = 4, it takes 4 iterations. Ie takes an iteration. Here, time complexity = O(n) times. Space complexity = O(1)
def fun3(n):
   sum = 0
   for i in range(1, n+1):
       for j in range(i, i+1):
        sum += 1
        return sum     
                            #This, if n = 4, there will be 10 iterations. This is nested loop. Time complexity = O(n * n). (Quadratic growth). Space complexity = O(1)

#1st funtion is the best and fastest (Formula method). 2nd function is the medium one (Loop method). 3rd function is the slowest one(Nested loop).

#Graph anylasis:..For func 1, it's a flat line. Here, time does not increase with n. 
                 #For func 2, graph is straight line. Here, time increases with n
                 #For func 3, graph grows much faster. Here, time increases with n square.