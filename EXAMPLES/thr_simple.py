
from threading import Thread, Lock
import random
import time

STDOUT_LOCK = Lock()

class SimpleThread(Thread):
    def __init__(self, num):
        super().__init__()  # call base class constructor -- REQUIRED
        self._threadnum = num

    def run(self):  # the function that does the work in the thread
        time.sleep(random.randint(1, 3))
        with STDOUT_LOCK:
            print("Hello from thread {}".format(self._threadnum))

thread_list = []

for i in range(16):
    t = SimpleThread(i)  # create the thread
    t.start()  # launch the thread
    thread_list.append(t)

print(f"thread_list: {thread_list}")
for t in thread_list:
    t.join()  # wait for thread to finish

print("All threads are finished")
