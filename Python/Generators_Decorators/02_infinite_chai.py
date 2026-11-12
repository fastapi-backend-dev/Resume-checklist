"""
Simple explanation of this program:

This program creates an infinite generator, which means it keeps producing values
forever unless we stop it manually.

A generator is a special type of function that uses `yield` instead of `return`.
When Python sees `yield`, it does not end the function completely. Instead, it
pauses the function and remembers its current state. The next time we call
`next(...)`, the function continues from where it left off.

In this example:
- `infinite_chai()` creates a generator object.
- `count` starts at 1.
- The loop runs forever because `while True` is always true.
- Each time the generator runs, it yields a message like "Refill #1".
- After yielding, the function pauses.
- When we call `next(...)` again, it resumes, increases the count, and produces
  the next message.

This is useful when we need a stream of values without storing them all in memory.

Interview Questions and Answers:

Q1. What is a generator in Python?
A1. A generator is a function that uses `yield` to produce values one at a time.
    It does not return all values at once like a list.

Q2. What is the difference between `return` and `yield`?
A2. `return` ends the function and sends back one final value. `yield` pauses the
    function and allows it to continue later, producing values step by step.

Q3. Why is this program called an infinite generator?
A3. Because the while loop is always true, so it keeps generating new values forever.
    We can stop it by breaking the loop or by limiting how many times we call next().

Q4. What does `next(refill)` do?
A4. It asks the generator for the next value. The generator resumes from its last
    paused point and returns the next item.

Q5. Why are there two generator objects, `refill` and `user`?
A5. Because each generator object keeps its own separate state. `refill` and `user`
    both start counting from 1, but they are independent of each other.
"""


# This function is a generator function.
# Instead of returning a full list, it produces values one by one.
def infinite_chai():
    # Start counting from 1.
    count = 1

    # This loop never ends on its own.
    # It keeps creating new values forever.
    while True:
        # `yield` sends a value to the caller and pauses the function.
        # The program stays in this state until `next()` is called again.
        yield f"Refill #{count}"

        # Increase the count after each yield.
        count += 1


# Create the first generator object.
# This object remembers its own state.
refill = infinite_chai()

# Create a second generator object.
# This is independent from the first one.
user = infinite_chai()

# Ask for the first 3 values from the refill generator.
for _ in range(3):
    print(next(refill))

# Print a separator line to make the output easier to read.
print("-------------------------------------")

# Ask for the first 5 values from the user generator.
for _ in range(5):
    print(next(user))

# Explanation of the output:
# The first generator prints:
# Refill #1
# Refill #2
# Refill #3
#
# Then the second generator prints:
# Refill #1
# Refill #2
# Refill #3
# Refill #4
# Refill #5
#
# Even though both generators use the same function, they do not share the same
# count value because each generator object has its own memory and state.
