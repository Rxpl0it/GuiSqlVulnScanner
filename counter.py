from threading import Lock

class Counter:
    def __init__(self, label):
        self.count = 0
        self.label = label
        self.lock = Lock()
        self.update_label()

    def increment(self):
        with self.lock:
            self.count += 1
            self.update_label()

    def get_count(self):
        with self.lock:
            return self.count

    def update_label(self):
        self.label.config(text=str(self.count))
