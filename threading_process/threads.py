# three ways to create a thread in python
# 1.creating a thread without using any class
# 2. creating a thread by extending thread class
# 3. creating a thread without extending thread class



import threading

def f(x):
    print(x**2)

def sum(a,b):
    print(a+b)

if __name__ == '__main__':

    t1 = threading.Thread(target = f, args=(5,))
    t1.start()

    t2 = threading.Thread(target = sum, args=(10,20))
    t2.start()
