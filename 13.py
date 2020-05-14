nums = []

for i in range(4):
  nums.append(int(input()))

max_ = nums[0]

for i in range(1,4):
  if max_ <= nums[i]:
    max_ = nums[i]

print(max_)

nums.append(int(input()))

max_ = nums[0]

for i in range(1,5):
  if max_ <= nums[i]:
    max_ = nums[i]

print(max_)