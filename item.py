import csv

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    all = []
    def __init__(self, name: str, price: float, quantity): #constructor- the __init__ is called everytime an object is created from a class.
        assert price >=0, f"Price {price} is not greater than 0!" #(Assert is a statement used to ensure if there is a match with what is happening to your expectations)
        assert quantity >=0, f"Quantity {quantity} is not greater or equal to zero!"
        self.__name = name #self is used to access variables referenced in a class
        self.__price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property #property- read only attribute   
    def name(self):
        return self.__name
    
    @name.setter  #setter used to set a new value even when a read only attribute is used
    def name(self, value):
        if len(value) >10:
            raise Exception("Name is  too long!")
        else:
            self.__name=value

    def calc_total_price(self):#functions inside classes are known as methods
        return self.__price * self.quantity
    
    

    @classmethod #decorated used to change a function's working.
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod        
    def is_integer(num):
        #100.0 will not be considered a float.
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    @property
    def read_only_name(self):
        return "AAA"   

    def __repr__(self): #__repr__ is used to represent an object
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
    def __connect(self):
        pass
    
    def __prepare_body(self):
        return f""" Hello Someone.
        We have  {self.name} {self.quantity} times.
        Regards."""

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()

        
# A double underscore is used to make private methods (known as abstraction).

    
