def process_order(item, quantity):
    try:
        price = {"masala": 25}[item]
        cost = price * quantity
    except KeyError:
        print("chai type is not present")
    except TypeError:
        print("quantity must be integer")


process_order("ginger", 5)
process_order("masala", "two")
