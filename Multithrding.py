
"""
multi-threaded program contains two or more parts that can run concurrently and each part can
handle a different task at the same time making optimal use of the available resources
specially when your computer has multiple cpu's

multithreaded enable us to write in a way where multiple activities can proceed
concurrently in the same program

thread - is an entity within a process that can be scheduled for execution. or is a subset of program


"""

import threading
print("Demonstration of multithreading")
def fun(number):
    for i in range(number):
        print(i)
def gun(number):
    for i in range(number):
        print(i)
if __name__ == "__main__":
    number = 5
    thread1 = threading.Thread(target = fun,args = (number,))
    thread2 = threading.thread(target = gun,args = (number,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
