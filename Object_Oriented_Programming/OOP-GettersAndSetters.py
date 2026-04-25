class Movie:
    
    def __init__(self, title, rating):
        self._title = title
        self.rating = rating
        
    def get_title(self):
        return self._title
    

MyMovie = Movie('The Godfather', 8.7)
MyMovie.get_title()

class Dog:
    
    def __init__(self, name, breed):
       self._name = name
       self.breed = breed
       
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        if isinstance(new_name , str) and new_name.isalpha():
            self._name = new_name
        else:
            print(f'that name is not a valid name')

MyDog = Dog('Morteza', 'Golden')
MyDog.get_name()
MyDog.set_name('lou343')



class Backpack():
    
    def __init__(self):
        self._items = []
        
    def get_items(self):
        return self._items
    
    def set_items(self , new_items):
        # with setter we can update the non-public attributes
        if isinstance(new_items, list):
             self._items = new_items
        else : print('not a valid items')


MyPack = Backpack()
MyPack._items

MyPack.set_items(['pencil', 'wallet'])
MyPack.get_items()


