# def update(a=9):
#     a=8
#     print(a)
# update(2)

#different types of function arguments
#1.positional args
#2.keyword args
#3.default args
#4.variable length args
#keywordvariable length args

#1.positional args
def person(name,age):
    print("positional args....",name,age,end='')
    print()
person('siva',25)

#2.keyword args
def person1(name,age):
    print('keyword args....',name,age,end='')
person1(age=25,name='sai')

#3.default args
def person2(name,age=18):
    print()
    print("default args.....",name,age,end='')

person2(name="suri")

#4.variable length args
def add(a,*b):
    print()
    c = a
    for d in b:
        c=c+d
    print("variable length:",c)
add(10,20,30,40)

#keywordvariable length args
def person_details(**deatils):
    print(deatils)


person_details(name='siva',age=25,address='ap',mob=111111)
