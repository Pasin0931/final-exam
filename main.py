class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}")
            
class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address

    def place_order(self, item):
        return DeliveryOrder(self.name, item, "preparing")
    
class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self, other, order):
        print(f"{self.name} is delivering {order} to {other.name} using {self.vehicle}")
        
class DeliveryOrder:
    def __init__(self, customer, item, status="preparing"):
        self.customer = customer
        self.item = item
        self.status = status
        
    def assign_driver(self, driver):
        print(f"New driver assigned: {driver.name}")
    
    def summary(self):
        return f"Customer name: {self.customer} | Order: {self.item} | Status: {self.status}"
    
customer_1 = Customer("Alice", "abc")
customer_2 = Customer("Bob", "abb")

driver_1 = Driver("David", "motorcycle")

customer_1.introduce()
customer_2.introduce()
driver_1.introduce()