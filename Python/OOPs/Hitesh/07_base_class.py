class Chai:
    def __init__(self, name, price):
        # Base class constructor sets common attributes for all chai types.
        self.name = name
        self.price = price


# 1) Accessing base class by duplicating code.
# This works, but it repeats the same logic and is not recommended.
# It manually copies the base class attributes into the child class.
# class GingerChai(Chai):
#     def __init__(self, name, price, ginger_amount):
#         self.name = name
#         self.price = price
#         self.ginger_amount = ginger_amount


# 2) Accessing base class by calling the parent class directly.
# This is clear and works well, but it couples the child class to the exact base class name.
# Example: `Chai.__init__(self, name, price)` calls the parent constructor directly.
# class GingerChai(Chai):
#     def __init__(self, name, price, ginger_amount):
#         Chai.__init__(self, name, price)
#         self.ginger_amount = ginger_amount


# 3) Accessing base class using super().
# This is the recommended and modern way in Python.
# `super()` automatically finds the parent class and calls its constructor.
# It is cleaner and supports inheritance more safely.
class GingerChai(Chai):
    def __init__(self, name, price, ginger_amount):
        super().__init__(name, price)
        self.ginger_amount = ginger_amount
