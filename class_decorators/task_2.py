# You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers.  
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, 
# use getters and setters instead!

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_new_worker(self, worker):
        self.workers.append(worker)
        return self.workers
 
    def __str__(self):
        return self.name

class Worker:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = ""

    def get_boss(self):
        return self._boss

    def set_boss(self, boss):
        is_boss_the_instance = isinstance(boss, Boss)
        if is_boss_the_instance:
            self._boss = boss
        else:
            print("The passed boss is not an instance of Boss class")

    def __str__(self):
        return f"Name: {self.name}, company: {self.company}, boss: {self.boss}"

    boss = property(get_boss, set_boss)

boss_1 = Boss(10, "Anastasiia", "SoftServe")
worker_1 = Worker(15, "John", "SoftServe")
worker_2 = Worker(20, "Jane", "SoftServe")
worker_1.boss = boss_1
worker_2.boss = "Anastasiia Andrieieva"
print(worker_2)