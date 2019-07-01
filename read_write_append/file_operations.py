# f1=open('S:/file operations/test.txt','r')
# print(f1.read())
#
# f2=open('S:/file operations/sss.csv','r')
# print(f2.read())
import csv

# f2=open('S:/file operations/sss3.csv','w')
# print(f2.write("101,siva,25,30000,hyd"))

f1=open("some_file_1.txt","r")
f2=open("some_file_2.txt","r")
for line1 in f1:
    for line2 in f2:
        if line1==line2:
            print("SAME\n")
            print(line1, '+',line2 )
        # else:
        #     print(line1 + line2)
        break
f1.close()
f2.close()