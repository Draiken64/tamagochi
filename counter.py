class Counter:
    quantity =0


    def __init__(self):
        Counter.quantity += 1
        self.number = Counter.quantity

    def __del__(self):  # destruktor
        Counter.quantity -= 1

    @staticmethod
    def count():
        return Counter.quantity

a = Counter()
print(a.number)
a = None
print(Counter.quantity)