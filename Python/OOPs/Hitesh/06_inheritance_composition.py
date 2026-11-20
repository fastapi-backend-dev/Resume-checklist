"""
Easy explanation of Inheritance and Composition

Inheritance:
    Inheritance means a child class gets features from a parent class.
    Example: A `MasalaChai` is a kind of `BaseChai`, so it can use the `prepare()` method.
    Analogy: Like a child inheriting eye color or height from parents.

Composition:
    Composition means a class contains another object and uses it.
    Example: A `ChaiShop` has a `chai` object inside it.
    Analogy: Like a car having an engine. The car is not the engine, but it uses the engine.

Easy difference:
    - Inheritance: "is-a" relationship.
      Example: `MasalaChai` is a `BaseChai`.
    - Composition: "has-a" relationship.
      Example: `ChaiShop` has a `chai`.

Why this matters:
    Inheritance is useful when classes are closely related.
    Composition is useful when one class uses another object to do work.

10 common interview questions and answers:

1. What is inheritance in OOP?
   Answer: It is when a class gets attributes and methods from another class.

2. What is composition in OOP?
   Answer: It is when one class contains an instance of another class and uses it.

3. What is the difference between inheritance and composition?
   Answer: Inheritance is "is-a"; composition is "has-a".

4. When should we use inheritance?
   Answer: When there is a clear parent-child relationship and shared behavior.

5. When should we use composition?
   Answer: When we want flexibility and reuse without tightly coupling classes.

6. Is multiple inheritance allowed in Python?
   Answer: Yes, Python supports multiple inheritance.

7. What is a real-life example of inheritance?
   Answer: A `Dog` class can inherit from an `Animal` class.

8. What is a real-life example of composition?
   Answer: A `College` class can have many `Student` objects.

9. Which is better: inheritance or composition?
   Answer: Composition is often more flexible, but inheritance is useful for clear hierarchies.

10. Can a class use both inheritance and composition together?
    Answer: Yes, many systems do both.
"""


# Base class for all chai types.
# It stores the type of chai and defines a method to prepare it.
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai.")


# MasalaChai inherits from BaseChai.
# This means it gets the `prepare()` method from the parent class.
# It also adds its own behavior with `add_spices()`.
class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, and cinnamon.")


# ChaiShop is a class that creates and uses a chai object.
# It follows composition because the shop contains a `chai` object.
# The `chai_cls` attribute decides which kind of chai is used in the shop.
# `chai_cls` is a class attribute, not an instance attribute.
# It stores a class, such as `BaseChai` or `MasalaChai`, instead of a single value.
# This is a common design pattern: the parent class decides which object to create,
# while a child class can override that class attribute to change behavior.
class ChaiShop:
    # `chai_cls` tells the shop which chai class to create.
    # Default is `BaseChai`, so regular shops make regular chai.
    chai_cls = BaseChai

    def __init__(self):
        # `self.chai_cls` is looked up on the instance, then on the class.
        # So this creates an object of the class stored in `chai_cls`.
        # Example: `self.chai_cls("Regular")` creates a `BaseChai("Regular")` object.
        self.chai = self.chai_cls("Regular")

    def serve(self):
        # `self.chai.type` means: access the `type` attribute of the chai object.
        # This gives the chai's name, such as "Regular".
        print(f"Serving {self.chai.type} chai in the shop")

        # `self.chai.prepare()` means: call the `prepare()` method of the chai object.
        # This method is defined in `BaseChai` and is inherited by `MasalaChai`.
        self.chai.prepare()


# FancyChaiShop inherits from ChaiShop.
# It changes the chai type by assigning a different `chai_cls`.
# This is an example of reusing behavior through inheritance and overriding a class attribute.
# Since `FancyChaiShop.chai_cls = MasalaChai`, every new fancy shop creates a MasalaChai object.
class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai



# Create a normal chai shop.
# `shop.chai` is an instance of `BaseChai` because `ChaiShop.chai_cls = BaseChai`.
shop = ChaiShop()

# Create a fancy chai shop.
# `fancy.chai` is an instance of `MasalaChai` because `FancyChaiShop.chai_cls = MasalaChai`.
fancy = FancyChaiShop()

# Serve regular chai.
# `shop.serve()` calls `self.chai.prepare()` on the regular chai object.
shop.serve()

# Serve fancy chai.
# `fancy.serve()` calls `self.chai.prepare()` on the masala chai object.
fancy.serve()

# `fancy.chai.add_spices()` works because `fancy.chai` is actually a `MasalaChai` object.
# The object has both the inherited `prepare()` method from `BaseChai`
# and its own custom `add_spices()` method defined in `MasalaChai`.
# This is a good example of dynamic behavior: the same shop method works,
# but the actual chai object changes based on the class attribute.
fancy.chai.add_spices()
