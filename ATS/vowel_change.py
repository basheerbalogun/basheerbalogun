c = input(': ')
newstr = c
vowels = ('a', 'e', 'i', 'o', 'u')
for char in c.lower():
    if vowels in c:
        c.replace(vowels, "@")
    print(c)
        