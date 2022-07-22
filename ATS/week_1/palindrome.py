

def palindrome(num):
    tem=num
    rev=0
    while tem > 0:
        r = tem % 10
        rev = rev *10 +r
        tem = tem // 10
    if rev== num:
        print(num ,"it is palindrome")
    else:
        print(num, "it is not palindrome")
palindrome(int(input(": ")))