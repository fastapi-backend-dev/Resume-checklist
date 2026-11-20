# self is like saying: "this exact object that is calling me."
# Imagine a class is a blueprint for a cup, and each cup object is a real cup.
# When you call cup.describe(), Python gives the method the current cup object
# as the first argument, and Python calls that argument self.
# So self is just a reference to the current object.
# Example: if there are 2 cups, cup1 and cup2, then:
#   cup1.describe() uses self = cup1
#   cup2.describe() uses self = cup2
# This is like saying: "look at THIS cup, not all cups." 

class ChaiCup:
    # Class attribute: shared by all cups unless changed in one instance.
    cup_size = 150  # ml

    # self means: "this current object"
    # It lets the method work with the specific cup instance calling it.
    def describe(self):
        # self.cup_size means: use the cup_size value for this object.
        return f"This cup can hold {self.cup_size} ml of tea."


# Create one object of the class.
cup = ChaiCup()
print(cup.describe())
# This is the same as the above call: Python passes the object automatically.
print(ChaiCup.describe(cup))

# Create another object and change only its own value.
cup2 = ChaiCup()
cup2.cup_size = 200
print(ChaiCup.describe(cup2))
