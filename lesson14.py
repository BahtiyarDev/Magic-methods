# class Book:
#     def __init__(self, name, author, pages):
#         self.name = name
#         self.author = author
#         self.pages = pages

#     def get_info(self):
#         return f'{self.name} by {self.author}'
    
#     def __str__(self):                       
#         """при обращении к экземпляру выдает инфу о нем"""
#         return f"{self.name} by {self.author}"
    
#     def __repr__(self):                       
#         """однозначные комменттарии про экземпляр для разработчика"""
#         return f"{self.name} by {self.author}"
    
#     def __eq__(self, value):
#         return self.pages == value.pages
#     def __lt__(self, other):
#         return self.pages < other.pages
    
#     def __add__(self, other):
        
#         return self.pages + other.pages
    
#     def __gt__(self, other):
#         return self.pages > other.pages
        
    
    

# book1 = Book('1984', 'George Orwell', 550)
# book2 = Book('War and Peace', 'Leo Tolstoy', 1400)
# # print(book1.get_info()) 
# print(book1)

# print(repr(book1))

# print(book1 == book2)
# print(book1 < book2)

# print(book1 + book2)


# __add__, __eq__, __ls__, __gt__

class Time:
    def __init__(self, hrs, mnt):
        self._hrs = hrs
        self._mnt = mnt
        self._format()

    def __str__(self):
        return f'Now {self._hrs}:{self._mnt}'
    
    def __repr__(self):
        return f'Now {self._hrs}:{self._mnt}'
    
    def __eq__(self, other):
        return self._hrs == other._hrs and self._mnt == other._mnt
    
    def  _format(self):
        if self._mnt >= 60:
            self._hrs += self._mnt//60
            self._mnt = self._mnt%60
        self._hrs %= 24

    
    def __add__(self, other):
        return Time((self._hrs+other._hrs), (self._mnt + other._mnt))
        
    

        
    

time1 = Time(21, 120)
time2 = Time(5, 14)
# print(time1 == time2)
print(time1 + time2)
    

        