import threading
import time
import random

rw_mutex = threading.Semaphore(1)  # writer_mutex
mutex = threading.Semaphore(1)     # read_count mutex
read_count = 0  
shared_data = 0

def reader(id):
    global read_count
    while True:
        time.sleep(random.uniform(0.5, 2))

        mutex.acquire()  # cam key1-> sua read_count
        read_count += 1
        if read_count == 1:  # cam key2-> chan Writer
            rw_mutex.acquire()
        mutex.release() # bo key1

        print(f"Reader {id} doc du lieu: {shared_data}")

        mutex.acquire()
        read_count -= 1
        if read_count == 0:  # bo key2, cho Writer ghi
            rw_mutex.release()
        mutex.release()

def writer(id):
    global shared_data
    while True:
        time.sleep(random.uniform(1, 3))  

        rw_mutex.acquire()  
        shared_data += 1 
        print(f"Writer {id} ghi du lieu: {shared_data}")
        rw_mutex.release()  

num_readers = 5
num_writers = 2

reader_threads = [threading.Thread(target=reader, args=(i,)) for i in range(num_readers)]
writer_threads = [threading.Thread(target=writer, args=(i,)) for i in range(num_writers)]

for t in reader_threads + writer_threads:
    t.start()
for t in reader_threads + writer_threads:
    t.join()
