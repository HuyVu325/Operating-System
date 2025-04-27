import threading
import time
import random

BUFFER_SIZE = 5
buffer = []

# Semaphore
mutex = threading.Semaphore(1)    
full = threading.Semaphore(0)     
empty = threading.Semaphore(BUFFER_SIZE)  

def producer():
    global buffer
    for i in range(10): 
        item = f"Item-{i}"
        empty.acquire()  
        mutex.acquire()  # Khóa buffer

        buffer.append(item)
        print(f"Producer -> Đã sản xuất: {item}")

        mutex.release()  # Mở khóa buffer
        full.release()   # Báo có dữ liệu cho Consumer

        time.sleep(random.uniform(0.1, 0.5))  #

# Consumer function
def consumer():
    global buffer
    for _ in range(10):  
        full.acquire()  
        mutex.acquire()  # Khóa buffer 

        item = buffer.pop(0)
        print(f"Consumer <- Đã tiêu thụ: {item}")

        mutex.release()  # Mở khóa buffer
        empty.release()  # Báo cho Producer rằng buffer có chỗ trống

        time.sleep(random.uniform(0.1, 0.5))  

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("Kết thúc chương trình.")
