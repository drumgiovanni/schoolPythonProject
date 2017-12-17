class Item(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Cart(object):
    def __init__(self):
        self.item = Item
    def listing(self):
        list = {}