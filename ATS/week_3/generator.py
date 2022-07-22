def loop():

    l = [1,2,3,4]

    for i in l:
        yield i
f=loop()
print(next(f))
print(next(f))


def generator():
    d = {'n': 2, 'h':5,'g':6}
    for v in d.values():
        print(type(v))


def open():
    with open("hang_man.txt", 'r') as file:
        read = file.readline()
        for row in read:
            yield row
        
