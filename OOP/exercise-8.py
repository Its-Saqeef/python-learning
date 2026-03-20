#Create a class ShoppingCart that stores items and their prices. Add methods to add items and calculate total.

class ShopingCart():
    def __init__(self):
        self.cart = []

    def add_item(self,name,price,quantity):
        self.cart.append({
            "name" : name,
            "price" : price,
            "quantity" : quantity
        })

        print("Item Added",self.cart)
    
    def calculate_total(self):
        total = 0
        for item in self.cart:
            total += item["price"] * item["quantity"]
        
        return total
                

cart = ShopingCart()
cart.add_item("Shopping bag",100,5)

total = cart.calculate_total()
print(total)