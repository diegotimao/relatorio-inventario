from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, prod):
        self.prod = prod
        self.index = 0

    def __next__(self):
        try:
            products = self.prod[self.index]
        except IndexError:
            raise StopIteration()
        else:
            self.index += 1
            return products
