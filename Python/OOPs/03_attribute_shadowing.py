class Chai:
    # Class-level attributes: shared by all objects of this class.
    temperature = "hot"
    strength = "strong"


cutting = Chai()
# Instance reads the class value when it has no own value yet.
print(f"Cutting tea temperature: {cutting.temperature}")  # hot

# Shadowing: instance attribute hides the class attribute with the same name.
cutting.temperature = "mild"
cutting.cup = "small"

# Now the instance value is used instead of the class value.
print(f"Cutting tea temperature after modification: {cutting.temperature}")  # mild
# The class attribute still remains unchanged.
print(f"Class attribute temperature: {Chai.temperature}")  # hot
# New instance attribute is created only for this object.
print(f"Cutting tea cup size: {cutting.cup}")  # small

del cutting.temperature
# After deleting the instance value, Python falls back to the class value again.
print(f"Cutting tea temperature after deletion: {cutting.temperature}")  # hot

del cutting.cup
# This attribute existed only on the instance, so it is gone.
print(f"Cutting tea cup size after deletion: {cutting.cup}")  # AttributeError: 'Chai' object has no attribute 'cup'
