import threading

class Counter(threading.Thread):
    def __init__(self):
        super().__init__()
    
    def run(self):
        global counter
        for _ in range(rounds):
            with counter_lock:
                counter += 1

if __name__ == "__main__":
    counter = 0
    rounds = 100000
    counter_lock = threading.Lock()

    thread1 = Counter()
    thread2 = Counter()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"The final counter value is: {counter}")
