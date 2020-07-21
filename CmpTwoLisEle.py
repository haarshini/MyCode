a = []
b = []

a = [int(item) for item in input().split()]
b = [int(item) for item in input().split()]

def trip(a,b):
    compare = [0,0]
    for i in range(0, len(a)):
        if a[i] > b[i]:
            compare[0] += 1
        elif a[i] < b[i]:
            compare[1] += 1
        else:
            pass
    return '{}{}'.format(compare[0],compare[1])

print(trip(a,b))