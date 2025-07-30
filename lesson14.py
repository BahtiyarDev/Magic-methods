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
        self.hrs = hrs
        self.mnt = mnt

    def __str__(self):
        return f'Now {self.hrs}:{self.mnt}'
    
    def __repr__(self):
        return f'Now {self.hrs}:{self.mnt}'
    
    def __eq__(self, other):
        return self.hrs == other.hrs and self.mnt == other.mnt
    
    def __add__(self, other):

        # if self.hrs + other.hrs <= 24 and self.mnt + other.mnt <= 60:
        #     return self.hrs + other.hrs, self.mnt + other.mnt
        
        if self.hrs + other.hrs <= 24 and self.mnt + other.mnt > 60:
            return self.hrs + other.hrs + (self.mnt + other.mnt)//60, (self.mnt + other.mnt)%60
        
        elif self.hrs + other.hrs > 24 and self.mnt + other.mnt > 60:
            return (self.hrs + other.hrs)%24 + (self.mnt + other.mnt)//60, (self.mnt + other.mnt)%60
        
        else:
            return self.hrs + other.hr, self.mnt + other.mnt

        
    

time1 = Time(20, 54)
time2 = Time(5, 14)
# print(time1 == time2)
print(time1 + time2)
    

        