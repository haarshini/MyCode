n = int(input("enter val:"))
count = 0 
while (n>0):
	n = n // 10 # n divided by 10
	count = count + 1

print(count)

#method 2

print("count is ",len(str(abs(n))))