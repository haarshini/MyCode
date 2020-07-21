n=int(input("enter a num:"))
def palindrome(n):
  i = 0
  while True:
    k = str(n)
    if k == k[::-1]:
      break
    else:
      m = int(k[::-1])
      n = n + m
      i = i + 1
  return n 
print(palindrome(n))




    
