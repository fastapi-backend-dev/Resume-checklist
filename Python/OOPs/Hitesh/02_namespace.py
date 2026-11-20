class Chai:
    # Class namespace: this value belongs to the class itself,
    # so every object of Chai can access it.
    origin = "India"


# Accessing a class attribute from the class namespace.
print(Chai.origin)  # India

# Adding a new attribute to the class namespace.
Chai.is_hot = True
print(Chai.is_hot)  # True

# Creating an instance of Chai.
# The instance has its own namespace, but it can also see the class namespace.
ginger_tea = Chai()
print(f"Ginger tea origin: {ginger_tea.origin}")  # India
print(f"Ginger tea is hot: {ginger_tea.is_hot}")  # True

# Instance namespace: this value is stored only for this object.
# It does not change the class attribute.
ginger_tea.is_hot = False

print(f"Class: {Chai.is_hot}")
print(f"Ginger tea instance: {ginger_tea.is_hot}")

# Another example of instance namespace: flavor belongs only to this object.
ginger_tea.flavor = "Ginger"
print(f"Ginger tea flavor: {ginger_tea.flavor}")
