from lib import Customer, Driver

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