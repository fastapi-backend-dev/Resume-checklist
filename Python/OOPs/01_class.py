class Chai:
    pass


class ChaiTime:
    pass


print(type(Chai))  # <class 'type'>

ginger_tea = Chai()
print(type(ginger_tea))  # <class '__main__.Chai'>
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
