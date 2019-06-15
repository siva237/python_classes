from multiprocessing import Process

def f(x):
    print(x**2)

def sum(a,b):
    print(a+b)

if __name__ == "__main__":

    p1 = Process(target = f, args = (5,))
    p1.start()

    p2 = Process(target = sum, args = (10,20))
    p2.start()

