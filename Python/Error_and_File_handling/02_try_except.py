orders = {"masala": 35, "ginger": 45}

try:
    print(orders["elaichi"])
except KeyError:
    print("Given chai type is not present...")

print("Done...")