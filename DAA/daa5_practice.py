import random


def partition(a, l, h, p):
    pivot = a[h]
    i = l - 1
    for j in range(l, h):
        if a[j] <= pivot:
            i += 1
            (a[i], a[j]) = (a[j], a[i])
    (a[i+1], a[h]) = (a[h], a[i+1])
    return i+1


def qs(a, l, h):
    if l < h:
        if randomized:
            piv = random.randrange(l, h)
        else:
            piv = h

        pi = partition(a, l, h, piv)
        qs(a, l, pi-1)
        qs(a, pi+1, h)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
randomized = True
qs(data, 0, size - 1)
print("Sorted Array in Ascending Order:")
print(data)
