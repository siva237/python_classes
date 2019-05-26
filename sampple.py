l1=[1,2,3]
l2=['one','two','three']
l3=[]
#output :[(1, 'one'), (2, 'two'), (3, 'three')]

# print(list(zip(l1,l2)))

for i in enumerate(l1):
    for j in enumerate(l2):
        if i[0]==j[0]:
            l3.append((i[1],j[1]))

print(l3)
