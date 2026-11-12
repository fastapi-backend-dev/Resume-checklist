def get_chai_order():
    # This function is a generator because it contains `yield`.
    # Its body starts running only when the generator is advanced.
    print("Welcome!! What type of chai do you want?")

    # Pause here until the caller sends the first order.
    # The value passed to .send(...) becomes the result of this `yield`,
    # so it is assigned to `order`.
    order = yield

    # Keep accepting orders. This is an endless loop, but it does not
    # run continuously: each `yield` pauses the generator and returns
    # control to the caller until the next .send(...) call.
    while True:
        print(f"Prepaing: {order}")

        # Pause after printing the current order.
        # The next value sent to the generator becomes the new `order`.
        order = yield


# Create the generator. This does not execute the function body yet.
stall = get_chai_order()

# Start the generator and run it up to its first `yield`.
# Calling next() is needed before sending the first non-None value.
next(stall)

# Resume the generator, supplying its first order.
# It prints the order and pauses at the next `yield`.
stall.send("Masala Chai")

# Resume it again with another order; the same loop repeats.
stall.send("Elaichi Chai")
