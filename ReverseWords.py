s = "hello.hello"

def rev(s):
	a = s.split(".")
	a = a[::-1]
	b = ".".join(a)
	print (b)
rev(s)