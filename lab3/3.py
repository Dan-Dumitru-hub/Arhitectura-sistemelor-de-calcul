from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from threading import current_thread
import time, random
 
data = ["A", "T", "G" , "C"]
v=[i for i in range(100)]

def modify_msg(msg):
	
	str1=str(v[msg])
	if listToString(data) in str1:
		return "DNA sequence found în sample"+str(current_thread())
  
def listToString(s): 
    
   
    str1 = "" 
    
    
    for ele in s: 
        str1 += ele  
    
    
    return str1 
 
def main():
	random.seed(random.randint(0,100))
	

	for i in range(100) :
		s=""
		for j in range(10000):
			s=s +(random.choice('ATGC'))


		v[i]=s
		
	for i in range(5):
		data.append(random.choice('ATGC'))
	
	
	s=range(100)
	with ThreadPoolExecutor(max_workers = 15) as executor:
		results = executor.map(modify_msg, s)
 
	for result in results:
		print(result)
 
if __name__ == '__main__':
	main()
	