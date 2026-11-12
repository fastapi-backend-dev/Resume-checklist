# This file shows how a decorator works in a simple way.
# A decorator is like a wrapper around a function. It adds extra behavior before and after
# the original function runs without changing the function's main purpose.
#
# How this code works from the top of the file:
# 1. Python imports the wraps tool from functools.
# 2. It defines log_activity(), which is the decorator.
# 3. It defines brew_chai(), the actual tea-making function.
# 4. Then it applies @log_activity above brew_chai.
# 5. Finally, it calls brew_chai("Masala").
#
# When Python reaches the line @log_activity, it does not run brew_chai directly.
# Instead, Python passes brew_chai into log_activity(). The decorator creates a new function
# called wrapper(), and wrapper() prints a message, calls the original function, and then prints
# another message after it finishes. This is the basic idea of a decorator.
#
# The decorator is useful because it lets us add logging or tracking to many functions without
# changing their code again and again.

from functools import wraps


# def log_activity(func):
# This is the decorator function.
# It takes one argument, func, which is the function that we want to decorate.
def log_activity(func):
    # @wraps(func)
    # This keeps the original function's name, docstring, and metadata when the wrapper replaces it.
    # Without it, the wrapper may hide the original function details.
    @wraps(func)
    # def wrapper(*args, **kwargs):
    # This is the new function created by the decorator.
    # It accepts any number of positional and keyword arguments and acts like a shell around the real function.
    def wrapper(*args, **kwargs):
        # print(f"🚀Calling: {func.__name__}")
        # This message is printed before the real function starts.
        # It tells us which function is being called.
        print(f"🚀Calling: {func.__name__}")
        # result = func(*args, **kwargs)
        # This line runs the original function with the same arguments that were passed to the wrapper.
        result = func(*args, **kwargs)
        # print(f"✅Finished: {func.__name__}")
        # This message is printed after the original function finishes.
        # It tells us the function completed successfully.
        print(f"✅Finished: {func.__name__}")
        # return result
        # The wrapper returns the same result that the original function produced.
        return result
    # return wrapper
    # When the decorator is used, it returns the wrapper function instead of the original one.
    return wrapper


# @log_activity
# This is decorator syntax.
# It means: take brew_chai and pass it into log_activity().
# Then replace brew_chai with the wrapper function returned by log_activity().
@log_activity
# def brew_chai(type, milk="no"):
# This is the real tea-making function.
# It accepts a tea type and an optional milk value.
def brew_chai(type, milk="no"):
    # print(f"Brewing {type} chai and milk status {milk}...")
    # This line does the actual work of the function: it prints the tea type and milk status.
    print(f"Brewing {type} chai and milk status {milk}...")


# brew_chai("Masala")
# This line calls the decorated function.
# Because of the decorator, Python runs the wrapper first, which prints the start message,
# then it executes the real brew_chai() function, and then prints the finish message.
brew_chai("Masala")
