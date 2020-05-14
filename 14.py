nums = [0,1,2,3,4,5,6,7,8,9]
name = ['a','b','c','d','e','f','g','h','i','j']

print(name)

print(dict(zip(nums,name)))

index = int(input())

for i in range(len(nums)):
  if index == i:
    print(name[i])

print(name[4:10])
print(name[3:])

n = int(input())

print(nums * n)

nums.extend(name)

print(nums)