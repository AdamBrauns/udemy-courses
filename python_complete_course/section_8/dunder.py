class Book():
    def __init__(self, tilte, author, pages):
        self.tilte = tilte
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f'{self.tilte} by {self.author}'

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object has been deleted")

b = Book('Minecraft good, Fortnite bad', 'Reddit', 365)

print(str(b))

print(len(b))

del b