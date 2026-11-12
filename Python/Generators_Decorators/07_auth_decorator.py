# This file demonstrates a decorator that checks a user's role before allowing access
# to a function. The decorator adds an access check without putting that check inside
# the protected function itself.
#
# How the file runs from top to bottom:
# 1. Python imports wraps, which helps the decorated function keep its original name and metadata.
# 2. Python defines require_admin(), the decorator that will perform the role check.
# 3. Python reaches @require_admin above access_tea_inventory and replaces that function with
#    the wrapper returned by the decorator.
# 4. The first call passes "user". The wrapper checks the role, prints an access-denied message,
#    and does not call the inventory function.
# 5. The second call passes "admin". The check succeeds, so the wrapper calls the original
#    inventory function, which prints the access-granted message.

# Import wraps so the decorator can preserve the original function's identifying information.
from functools import wraps


# Define a decorator that will check a role before running the function it receives.
def require_admin(func):
    # Keep the decorated function's name and other metadata on the wrapper.
    @wraps(func)
    # This wrapper runs whenever someone calls the decorated function.
    def wrapper(user_role):
        # Convert the role to lowercase so values like "ADMIN" and "Admin"
        # are treated the same as "admin".
        if user_role.lower() != "admin":
            # The role is not allowed, so explain why access was refused.
            print("Access denied: Admins only")
        else:
            # The role is allowed, so run the original function with the role argument.
            return func(user_role)
    # Give the wrapper back to Python to use in place of the original function.
    return wrapper


# Apply the require_admin decorator to this function.
# This is equivalent to: access_tea_inventory = require_admin(access_tea_inventory)
@require_admin
# Define the function that should only run for an admin.
def access_tea_inventory(role):
    # This message is printed only if the decorator allows the call through.
    print("Access granted to tea inventory...")


# Try calling the protected function as a regular user; access should be denied.
access_tea_inventory("user")
# Try again as an admin; the original function should run.
access_tea_inventory("admin")