class Counter:
    def __init__(self, label):
        self.count = 0
        self.label = label
        self.update_label()

    def increment(self):
        self.count += 1
        self.update_label()

    def get_count(self):
        return self.count

    def update_label(self):
        self.label.config(text=str(self.count))
