import threading
import time
import random

class DiningPhilosophers:
    def __init__(self, num):
        self.N = num
        self.THINKING = 0
        self.HUNGRY = 1
        self.EATING = 2

        self.state = [self.THINKING] * self.N
        self.mutex = threading.Lock()
        self.conditions = [threading.Condition(self.mutex) for _ in range(self.N)]
        # tao cho moi thread co notify and wait, dung chung 1 mutex lock

    # kiem tra
    def test(self, i):
        left = (i + self.N - 1) % self.N
        right = (i + 1) % self.N

        if self.state[i] == self.HUNGRY and self.state[left] != self.EATING and self.state[right] != self.EATING:
            self.state[i] = self.EATING
            self.conditions[i].notify()

    def pickup(self, i):
        with self.mutex:
            self.state[i] = self.HUNGRY
            print(f"Triet gia {i} dang doi va muon an")

            self.test(i)
            if self.state[i] != self.EATING:
                self.conditions[i].wait()

    def putdown(self, i):
        with self.mutex:
            self.state[i] = self.THINKING
            print(f"Triet gia {i} da an xong va dang suy nghi")

            self.test((i + self.N - 1) % self.N)
            self.test((i + 1) % self.N)

def philosopher(i, dining):
    while True:
        print(f"Triet gia {i} dang suy nghi...")
        time.sleep(random.uniform(1, 3))

        dining.pickup(i)

        print(f"Triet gia {i} dang an...")
        time.sleep(random.uniform(1, 2))

        dining.putdown(i)

#thinking -> hungry -> eating ->
# Tạo Monitor
dining = DiningPhilosophers(5)
philosophers = [threading.Thread(target=philosopher, args=(i, dining)) for i in range(5)]

for p in philosophers:
    p.start()
for p in philosophers:
    p.join()
