class Counter(object):
    def __init__(self):
        self.counter = 0
    def __str__(self):
        return f"[Counter] カウンターは{self.counter:d}"
    def up(self, x):
        self.counter += x
    def down(self, y):
        self.counter -= y

counter = Counter()
counter.up(4)
counter.down(1)
counter.up(38)
print(counter)
   