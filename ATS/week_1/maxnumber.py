number =[1,3,5,7,9,3,8]
#first solution
num = sorted(number)[-1]
print(num)


def max(a):
    res = a[0]
    for i in a:
        if res < i:
            res = i
    return res

array = (1, 2, 3, 4, 5, 6)
print(max(array))