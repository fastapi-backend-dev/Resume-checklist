class InvalidChaiOrder(Exception): pass


def chai_order(flavor, cups):
    try:
        menu = {"masala": 20, "ginger": 35}
        if flavor not in menu:
                raise InvalidChaiOrder(f"Invalid flavor: {flavor}. Only 'masala' and 'ginger' are allowed.")
        if not isinstance(cups, int) or cups <= 0:
            raise TypeError(f"Invalid number of cups: {cups}. Must be a positive integer.")
        total_cost = cups * menu[flavor]
        print(f"Order placed: {cups} cup(s) of {flavor} chai. Total cost: ${total_cost}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for your order!")


# Example usage:
chai_order("masala", 3)  # Valid order
chai_order("chocolate", 2)  # Invalid flavor
chai_order("ginger", -1)  # Invalid number of cups
chai_order("ginger", "two")  # Invalid type for cups
