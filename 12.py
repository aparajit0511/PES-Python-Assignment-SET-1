nums = []

for i in range(10):
  nums.append(int(input()))


average = sum(nums)//10

count_more_than_avg = 0
count_less_than_avg = 0
count_equal_avg = 0
print(average)
for i in range(10):
  if nums[i] > average:
    count_more_than_avg +=1
  elif nums[i] < average:
    count_less_than_avg +=1
  else:
    count_equal_avg +=1


print(count_more_than_avg,count_less_than_avg,count_equal_avg)