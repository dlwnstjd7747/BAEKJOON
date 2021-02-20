n = int( input())
a = 0
b = 0
x = n
cycle = 0

while (True):
   a = n//10 + n%10
   b = (n%10)*10 + (a%10)
   n = b
   cycle += 1
   if b == x :
       break
print(cycle)