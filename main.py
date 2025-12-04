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
    
customer_1 = Customer("Alice", "abc")
customer_2 = Customer("Bob", "abb")

driver_1 = Driver("David", "motorcycle")

customer_1.introduce()
customer_2.introduce()
driver_1.introduce()

order1 = customer_1.place_order("Laptop")
order2 = customer_2.place_order("Headphones")

order1.assign_driver(driver_1)
order2.assign_driver(driver_1)

print()
print(order1.summary())
print(order2.summary())

driver_1.deliver(customer_1, order1)
driver_1.deliver(customer_2, order2)

print("\nFinal Status:")
order1.check_status()
order2.check_status()