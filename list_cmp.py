def compare():
    l1=[1,2,3,4]
    l2=[2,3,1,4]
    # l1 = list(input("enter fir'st list:"))
    # l2 = list(input("enter first list:"))
    print(l1 is l2)
    print(l1 + l2)
    l1.sort()
    l2.sort()
    if l1 == l2:
        print("list are same")
    else:
        print("list not equal")
    d = {}
    print(d.fromkeys(l1))
    d1 = zip(l1,l2)
    print(dict(d1))


compare()

