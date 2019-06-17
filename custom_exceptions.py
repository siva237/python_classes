class Error(Exception):
    "Exception is the base class for all others"
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

class Test:

    number =10
    n = int(input("enter n value::"))
    try:
        if n < number:
            raise ValueTooSmallError

        elif n > number:
            raise ValueTooLargeError

        else:
            print("the given input matches the number")

    except ValueTooSmallError:
        print("The given input is too smaller, try again")

    except ValueTooLargeError:
        print("The given input is too large, try again")








