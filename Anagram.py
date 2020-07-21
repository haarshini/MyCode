a = input()
b = input()

def check (a,b):
	if sorted(a) == sorted(b):
		print("Yes")
	else:
		print("No")

check(a,b)