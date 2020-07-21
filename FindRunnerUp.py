 # to find second larger number (runnerup)
mylist = [2 ,3 ,6 ,6 ,5]
mylist = sorted(list(dict.fromkeys(mylist)))
print(mylist[-2])
