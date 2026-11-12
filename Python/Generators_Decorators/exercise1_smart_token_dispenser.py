def token_dispenser(start=1):
    try:
        token = yield
        while True:
            start += 1
            print(start)
            token = yield
    except:
        print("Dispenser closed")


my_gen = token_dispenser()
next(my_gen)

my_gen.send(5)
my_gen.send(4)

my_gen.close()