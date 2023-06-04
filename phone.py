from item import Item


class Phone(Item):#inheritance is used here so we can use all attributes of Item class.
     def __init__(self, name: str, price: float, quantity, broken_phones=0): #constructor- the __init__ is called everytime an object is created from a class.
        #Call to super function to have access to all attributes or methods
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >=0, f"Broken Phones {broken_phones} is not greater or equal to zero!"
        
        self.broken_phones = broken_phones