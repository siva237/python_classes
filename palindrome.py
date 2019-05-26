s = input("enter something:")


def palindrome(s='sissss'):
    print(s)
    reverse = s[::-1]
    if s == reverse:
        print(s, "is palindrome")

    else:
        print(s,"not palindrome")


palindrome(s)

