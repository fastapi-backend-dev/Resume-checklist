class ChaiOrder:
    # __init__ is called automatically when a new object is created.
    # It sets the object's starting values.
    # type_ is used instead of type because 'type' is a built-in Python name.
    # Using 'type' would confuse Python and may cause unexpected behavior.
    def __init__(self, type_, size):
        # self.type is the instance attribute (stored in this object)
        # type_ is the value passed in when creating the object.
        self.type = type_
        self.size = size

    def summary(self):
        # This method shows the order details for this specific object.
        return f"Chai Order: {self.size}ml {self.type} chai"


# Creating two different objects with different values.
order1 = ChaiOrder("Masala", 250)
print(order1.summary())

order2 = ChaiOrder("Ginger", 300)
print(order2.summary())
