import math

x = int(input())
y = int(input())
e = 2.71828
z = int(input())
h = ((x**(y+1) + e**(y-1)) / (1 + x*(abs(y - math.tan(z))))) * (1 + abs(y - x)) + ((abs(y - x)**2) / 2) - (abs(y - x)**3 / 3)
print(h)
