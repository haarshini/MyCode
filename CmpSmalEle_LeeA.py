nums = [8,1,2,2,3]
b = sorted(nums)
d= len(nums)
c = []
for i in nums:
    count = 0
    for j in b:
        if i > j:
            count += 1
    c.append(count)
print(c)