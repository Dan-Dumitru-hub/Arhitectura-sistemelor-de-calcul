import threading
import random
import time


class Philosopher(threading.Thread):
    running = True  
    def __init__(self, ids, leftfork, rightfork):
        threading.Thread.__init__(self)
        self.id = ids
        self.leftfork = leftfork
        self.rightfork = rightfork

    def run(self):
        while(self.running):
            
            time.sleep(random.randint(1,3))
            print ('Philosopher %s is hungry.' % self.id)
            fork1, fork2 = self.leftfork, self.rightfork

            while self.running:
                fork1.acquire() 
                locked = fork2.acquire(False) 
                if locked: 
                    break 
                fork1.release()
                fork2.release()
                
            else:
                return
            print ('Philosopher %s has both forks. '% self.id)
            time.sleep(random.randint(1,3))
            print ('Philosopher %s finishes eating.' % self.id)
            
            fork2.release()
            fork1.release()  
       
                
if __name__ == "__main__":
    nrphilosophers=10
    forks = [threading.Semaphore() for n in range(nrphilosophers)]
    philosophers= [Philosopher(i, forks[i%nrphilosophers], forks[(i+1)%nrphilosophers])
            for i in range(nrphilosophers)]

    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(10)
    Philosopher.running = False
    