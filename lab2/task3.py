"""
Coffee Factory: A multiple Cofeefactory - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the Cofeefactorys puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""


class Coffee:
    """ Base class """
    def __init__(self):
        pass

    def get_name(self):
        """ Returns the coffee name """
        raise NotImplementedError

    def get_size(self):
        """ Returns the coffee size """
        raise NotImplementedError


class ExampleCoffee:
    """ Espresso implementation """
    def __init__(self, size):
        pass

    def get_message(self):
        """ Output message """
        raise NotImplementedError


import sys
import random
import time
from threading import *

class Cofeefactory(Thread):
    def __init__(self, items, can_produce, can_consume,ids):
        Thread.__init__(self)
        self.items = items
        self.can_produce = can_produce
        self.can_consume = can_consume
        self.id=ids

    def produce_item(self):
        rand = random.randint(1,3)
        self.items.append(rand)
        if rand ==1:
            Americano.printtype(self.id)
        if rand ==2:
            Espresso.printtype(self.id)
        if rand ==3:
            Cappuccino.printtype(self.id)


   

    def run(self):
        while 1:
            time.sleep(random.randint(0, 10))
            self.can_produce.acquire()
            self.produce_item()
            self.can_consume.release()  

class Americano(Cofeefactory):
   
    def printtype(name):
        rand = random.randint(1,3)
        if rand == 1:
            print ("Factory {name} produced a small americano".format(name = name))
        if rand == 2:
            print ("Factory {name} produced a medium americano".format(name = name))


        if rand == 3:
            print ("Factory {name} produced a large americano".format(name = name))
class Espresso(Cofeefactory):
  
    def printtype(name):
        rand = random.randint(1,3)
        if rand == 1:
            print ("Factory {name} produced a small Espresso".format(name = name))
        if rand == 2:
            print ("Factory {name} produced a medium Espresso".format(name = name))


        if rand == 3:
            print ("Factory {name} produced a large Espresso".format(name = name))
class Cappuccino(Cofeefactory):
    
    def printtype(name):
        rand = random.randint(1,3)
        if rand == 1:
            print ("Factory {name} produced a small Cappuccino".format(name = name))
        if rand == 2:
            print ("Factory {name} produced a medium Cappuccino".format(name = name))


        if rand == 3:
            print ("Factory {name} produced a large Cappuccino".format(name = name))



class Consumer(Thread):
    def __init__(self, items, can_produce, can_consume,ids):
        Thread.__init__(self)
        self.items = items
        self.can_produce = can_produce
        self.can_consume = can_consume
        self.id=ids

    def consume_item(self):
        item = self.items.pop()
        if item == 1:
            item = "Americano"
        if item == 2:
            item = "Espresso"
        if item == 3:
            item = "Cappuccino"

        print ("Consumer {id} consumed {item}".format(id =self.id,item=item))

    

    def run(self):
        while 1:
            time.sleep(random.randint(0, 10))
            self.can_consume.acquire()
            self.consume_item()
            self.can_produce.release()



if __name__ == "__main__":

 

    count_Cofeefactory = int(100)
    count_consumers = int(100)
    buffer_length = int(100)

    items = []
    Cofeefactorys = []
    consumers = []

  
    can_produce = Semaphore(buffer_length)

    
    can_consume = Semaphore(0)

    for i in range(count_Cofeefactory):
        Cofeefactorys.append(Cofeefactory(items, can_produce, can_consume,i))
        Cofeefactorys[-1].start()

    for i in range(count_consumers):
        consumers.append(Consumer(items, can_produce, can_consume,i))
        consumers[-1].start()

    for p in Cofeefactorys:
        p.join()

    for c in consumers:
        c.join()