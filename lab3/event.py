from threading import enumerate, Event, Thread,Condition

ok=False

class Master(Thread):
    def __init__(self, max_work, work_available, result_available):
        Thread.__init__(self, name = "Master")
        self.max_work = max_work
        self.work_available = work_available
        self.result_available = result_available
        self.work=0
    
    def set_worker(self, worker):
        self.worker = worker
    
    def run(self):
        for i in range(self.max_work):

            # generate work
            self.work = i
            # notify worker
            global ok
            ok=True
            try:
                self.work_available.acquire()
                self.work_available.notify()
                # get result
                self.result_available.wait()
            except:
                break
           
            if self.get_work() + 1 != self.worker.get_result():
                print ("oops")
            print ("%d -> %d" % (self.work, self.worker.get_result()))
            
    
    def get_work(self):
        return self.work

class Worker(Thread):
    def __init__(self, terminate, work_available, result_available):
        Thread.__init__(self, name = "Worker")
        self.terminate = terminate
        self.work_available = work_available
        self.result_available = result_available
        
        


    def set_master(self, master):
        self.master = master
    
    def run(self):
        while(True):
            
            
            # wait work
            global ok
            if   ok:
                
                try:
                    self.work_available.wait()
                except:
                    break
                
                
                ok = True

                
            if(terminate.is_set()): 
                break
                    # generate result
            self.result = self.master.get_work() + 1
                    # notify master
            try:
                self.result_available.acquire()         
                self.result_available.notify() 
            except:
                break                     
    
    def get_result(self):
        return self.result



if __name__ ==  "__main__":
    # create shared objects
    terminate = Event()
    work_available = Event()
    result_available = Event()
    condition=Condition()
    
    # start worker and master
    w = Worker(terminate, condition, condition)
    m = Master(10, condition, condition)
    w.set_master(m)
    m.set_worker(w)
    w.start()
    m.start()

    # wait for master
    m.join()

    # wait for worker
    terminate.set()

    
    w.join()

    # print running threads for verification
    print(enumerate())

