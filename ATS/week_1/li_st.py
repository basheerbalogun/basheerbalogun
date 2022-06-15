a = [3, 1, 5, 2, 4]

for i in a[1:]:
    print(i)
    print("\n")
    j = a.index(i)
    print(j)
    print("\n")
    while j > 0 and a[j-1] > a[j]:  
        a[j], a[j-1] = a[j-1], a[j]
        j = j - 1
    print(j)