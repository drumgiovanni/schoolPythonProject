class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return f"[Book] {self.title} by {self.author}"
book1 = Book("「吾輩は猫である", "夏目漱石」")
book2 = Book("「人間失格", "太宰治」")

print(book1)
print(book2)
print(book1.title)
print(book2.author)