"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""
from threading import Thread
 
class MyThread(Thread):
    """ Clasa care incapsuleaza codul nostru concurent """
    def __init__(self, nr, msg):
        Thread.__init__(self)
        self.nr = nr
        self.msg = msg
 
    def run(self):
        print ("Thread", self.nr, "says:", self.msg)
 
# creeaza obiectele corespunzatoare thread-urilor
nr=int(input("cate thread"))
t=[MyThread(i, "hello from thread") for i in range(0,nr)]

	#t2 = MyThread(2, "hello from other thread")
 
# porneste thread-urile

for i in range(0,nr):
	t[i].start()
 
# executia thread-ului principal continua de asemenea
print ("Main thread says: hello from main")
 
# asteapta terminarea thread-urilor
for i in range(0,nr):
	t[i].join()

