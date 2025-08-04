# class Adder:
#     def __init__(self, add_value):
#         self.add = add_value

#     def __call__(self,adding):
#         return self.add + adding

#     def __add__(self, other):
#         return self.__call__(self) + other.__call__(self)


# add5 = Adder(5)
# print(add5(20))

# add100 = Adder(100)
# print(add100(100))

# print(add100(100) + add5(5))


# class Fraction:
#     def __init__(self, num, denom):
#         if denom == 0:
#             raise ValueError("Знаменатель не может быть равен нулю!")
#         common = self.gcd(num, denom)
#         self.num = num //common
#         self.denom = denom//common
#         self.formater()

#     def __str__(self):
#         return f'{self.num}/{self.denom}'

#     def formater(self):
#         if self.num % self.denom == 0:
#             return self.num / self.denom
#         else:
#             return f'{self.num}/{self.denom}'

#     @staticmethod
#     def gcd(a, b):
#         return a if b == 0 else Fraction.gcd(b, a%b)

#     def __add__(self, other):
#         return Fraction(self.num * other.denom + other.num * self.denom, self.denom * other.denom)
    
#     def __sub__(self, other):
#         return Fraction(self.num * other.denom - other.num * self.denom, self.denom * other.denom)
    
#     def __mul__(self, other):
#         return Fraction(self.num * other.num, self.denom * other.denom)
    
#     def __truediv__(self,other):
#         return Fraction(self.num * other.denom, self.denom * other.num)
    
#     def __eq__(self, other):
#         return self.num/self.denom == other.num/other.denom
    
#     def __lt__(self, other):
#         return self.num/self.denom < other.num/other.denom
    
#     def __gt__(self, other):
#         return self.num/self.denom > other.num/other.denom
        

# drob1 = Fraction(3, 2)
# drob2 = Fraction(4, 4)
# print(drob1 > drob2)


# import pickle

# data = [1, 2, 3]
# # .pkl
# with open("data.pkl", "wb") as f: #wb - write binary(редактирование на бинарном уровне)
#     pickle.dump(data, f)

# with open("data.pkl", "rb") as f: # rb - read binary(чтение на бинарном уровне)
#     print(pickle.load(f))


class Cache:
    def __init__(self, max_size):
        self.ch = []
        self.maxsize = max_size

    def __setitem__(self, key, value):
        self.ch.append({key:value})
        if len(self.ch) > self.maxsize:
            self.ch.pop(0)
    
    def __getitem__(self, key):
        for el in self.ch:
            if key in el.keys():
                return el[key]
            
    def __contains__(self, key):
        for el in self.ch:
            if key in el.keys():
                return True
        return False
    
    def __len__(self):
        return len(self.ch)
    
    def __delitem__(self, key):
        for el in self.ch:
            if key in el.keys():
                self.ch.remove(el)
        




cache = Cache(3)
cache['f'] = 52
cache['a'] = 'hello'
cache['c'] = 'bye'
del cache['a']
cache['g'] = 'hi'
print('d' in cache)
print(cache.ch)
print(len(cache))