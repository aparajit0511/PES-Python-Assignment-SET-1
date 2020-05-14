num = int(input())

a = 0
b = 1 
c = 0

print(a,b)

for i in range(num):
    c = a + b
    print(c)
    b = a
    a = c