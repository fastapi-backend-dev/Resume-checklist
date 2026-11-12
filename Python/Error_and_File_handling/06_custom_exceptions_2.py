class OutOfIngredientsError(Exception):
    pass


def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("No sugar or milk")
    print("Making chai...")


make_chai(2, 0)
