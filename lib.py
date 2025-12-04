class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self) -> None:
        print(f"Hi, I'm {self.name}.")
            
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

    def deliver(self, other, order) -> None:
        print(f"{self.name} is delivering {order.item} to {other.name} using {self.vehicle}.")
        order.status = "delivered"
        
class DeliveryOrder:
    def __init__(self, customer, item, status="preparing"):
        self.customer = customer
        self.item = item
        self.status = status
        
        self.this_driver = ""
        
    def assign_driver(self, driver) -> None:
        # print(f"New driver assigned: {driver.name}")
        self.this_driver = driver
    
    def summary(self):
        return f"Order Summary:\nItem: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.this_driver.name}\n"
    
    def check_status(self) -> None:
        print(f"Order for {self.item} -> {self.status}")