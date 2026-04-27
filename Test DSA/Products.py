class Product:
    def __init__(self,product_name,product_price):
        self.product_name = product_name
        self.product_price = product_price
        #self points directly to the object

    def get_name(self):
        return self.product_name
    
    def set_name(self,name):
        self.product_name = name

p1 = Product("Laptop", 256009)
print(p1.get_name())
p1.set_name("Gaming Laptop")
print(p1.get_name())
print(p1.product_price)

class Node:
    def __init__(self,product_name,product_price):
        self.product_name = product_name
        self.product_price = product_price
        self.next = None
