class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def get_info(self):
        return f'{self.name} by {self.author}'
    
    def __str__(self):                       
        """при обращении к экземпляру выдает инфу о нем"""
        return f"{self.name} by {self.author}"
    
    def __repr__(self):                       
        """однозначные комменттарии про экземпляр для разработчика"""
        return f"{self.name} by {self.author}"
    
    def __eq__(self, value):
        return self.pages == value.pages
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
        
    
    

book1 = Book('1984', 'George Orwell', 550)
book2 = Book('War and Peace', 'Leo Tolstoy', 1400)
# print(book1.get_info()) 
print(book1)

print(repr(book1))

print(book1 == book2)
print(book1 < book2)


# __add__, __eq__, __ls__, __gt__