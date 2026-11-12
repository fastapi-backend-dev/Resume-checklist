# try:
#     file = open("orders.txt", "w")
#     file.write("Order 1: 3 cups of masala chai\n")
# finally:
#     file.close()

with open("orders.txt", "w") as file:
    file.write("Order 1: 5 cups of elaichi chai\n")
