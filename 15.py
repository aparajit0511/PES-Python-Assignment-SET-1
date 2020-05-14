
name = ['a','b','c','d','e']

find = input()
if find in name:
  print("yes")
else:
  print("no")

for i in name:
  if find == i:
    print("yes")

print(name[::-1])