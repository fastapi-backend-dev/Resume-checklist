# This program demonstrates generators in a simple way.
# The functions local_chai(), imported_chai(), and full_menu() each produce items one at a time
# instead of returning everything at once. The generator chai_stall() waits for a drink order,
# and when close() is called it stops cleanly and prints a closing message.
#
# How the program runs: Python starts at the top of the file and executes statements in order.
# First, it defines the generator functions. Then it loops through full_menu() and prints each tea.
# After that, it creates stall = chai_stall(), calls next(stall) to start the generator, and then
# calls stall.close() to end it. In other words, the file runs top-to-bottom like a simple recipe.

# def local_chai():
# This defines a generator function named local_chai.
# A generator does not return a normal value immediately; it pauses and gives values one at a time.
# The function is only activated when it is iterated over.
def local_chai():
    # yield "Masala Chai"
    # This sends the first item, "Masala Chai", to the caller.
    # The function pauses here until the next iteration asks for the next value.
    yield "Masala Chai"
    # yield "Ginger Chai"
    # This sends the second item, "Ginger Chai", the next time the generator is resumed.
    yield "Ginger Chai"


# def imported_chai():
# This creates another generator for imported tea items.
# It is separate from local_chai() and yields a different set of values.
def imported_chai():
    # yield "Matcha"
    # This produces the first imported tea option.
    yield "Matcha"
    # yield "Oolong"
    # This produces the second imported tea option.
    yield "Oolong"


# def full_menu():
# This generator combines the outputs from two other generators.
# It essentially creates one full list of tea items from both local and imported selections.
def full_menu():
    # yield from local_chai()
    # This passes each item from local_chai() directly to the caller.
    yield from local_chai()
    # yield from imported_chai()
    # This passes each item from imported_chai() after the local items are exhausted.
    yield from imported_chai()


# def chai_stall():
# This generator simulates a chai stall that keeps waiting for customer orders.
# It stays active until the caller closes it manually with stall.close().
def chai_stall():
    try:
        # while True:
        # This loop runs forever so the stall keeps accepting new orders.
        while True:
            # order = yield "Waiting for chai order"
            # The generator yields the message "Waiting for chai order" to the caller.
            # When the caller sends a value back into the generator, it is stored in the variable order.
            # This lets the generator receive an order and continue processing.
            order = yield "Waiting for chai order"
    except:
        # print("Stall closed, no more chai...")
        # This runs only when the generator is closed by calling stall.close().
        # It prints a message to show the stall is shutting down.
        print("Stall closed, no more chai...")


# for chai in full_menu():
# This loops through every item produced by full_menu().
# Each item is assigned to the variable chai and printed one by one.
for chai in full_menu():
    # print(chai)
    # This displays the current tea name in the terminal.
    print(chai)

# stall = chai_stall()
# This creates a generator object for the chai stall but does not run it yet.
stall = chai_stall()
# print(next(stall))
# next(stall) starts the generator and runs until it reaches the first yield.
# The yielded string "Waiting for chai order" is printed to the screen.
print(next(stall))
# stall.close()
# close() raises a GeneratorExit inside the generator, which triggers the except block.
# This ends the generator cleanly and prints the closing message.
stall.close()
