#multithreaded priority queque in python.


#The Queue module is primarily used to manage to process large amounts of data on multiple threads. It supports the creation of a new queue object that can take a distinct number of items.
#The get() and put() methods are used to add or remove items from a queue respectively. Below is the list of operations that are used to manage Queue:

#get(): It is used to add an item to a queue.
#put(): It is used to remove an item from a queue.
#qsize(): It is used to find the number of items in a queue.
#empty(): It returns a boolean value depending upon whether the queue is empty or not.
#full(): It returns a boolean value depending upon whether the queue is full or not.
#A Priority Queue is an extension of the queue with the following properties:

#An element with high priority is dequeued before an element with low priority.
#If two elements have the same priority, they are served according to their order in the queue.
#Below is a code example explaining the process of creating multi-threaded priority queue:


import queue
import threading
import time

thread_exit_Flag = 0

class sample_Thread (threading.Thread):
def __init__(self, threadID, name, q):
	threading.Thread.__init__(self)
	self.threadID = threadID
	self.name = name
	self.q = q
def run(self):
	print ("initializing " + self.name)
	process_data(self.name, self.q)
	print ("Exiting " + self.name)

# helper function to process data		
def process_data(threadName, q):
while not thread_exit_Flag:
	queueLock.acquire()
	if not workQueue.empty():
		data = q.get()
		queueLock.release()
		print ("% s processing % s" % (threadName, data))
	else:
		queueLock.release()
		time.sleep(1)

thread_list = ["Thread-1", "Thread-2", "Thread-3"]
name_list = ["A", "B", "C", "D", "E"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for thread_name in thread_list:
thread = sample_Thread(threadID, thread_name, workQueue)
thread.start()
threads.append(thread)
threadID += 1

# Fill the queue
queueLock.acquire()
for items in name_list:
workQueue.put(items)

queueLock.release()

# Wait for the queue to empty
while not workQueue.empty():
pass

# Notify threads it's time to exit
thread_exit_Flag = 1

# Wait for all threads to complete
for t in threads:
t.join()
print ("Exit Main Thread")





