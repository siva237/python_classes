# a=int(input("enter a value::"))
# b=int(input("enter b value::"))
# try:
#     c=a/b
#     print(c)
# except Exception as e:
#     print(type(e).__name__)
# else:
#     print("NO errors in the business logic")
# finally:
#     print('finally block')


#custom exceptions
class CustomException(Exception):
    pass
class AgeError(CustomException):
    pass

while True:
    try:
        age = int(input("enter ur age:"))
        if age < 18 :
            raise AgeError
        break
    except CustomException:
        print('ur not eligible for vote')
print("ur eligble for vote")