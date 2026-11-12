def cache_results(func):
    d = {}
    def wrapper(n1, n2):
        result = func(n1, n2)
        if n1 in d.values() and n2 in d.values():
            print(True)
            
        d["n1"] = n1
        d["n2"] = n2
        d["result"] = result
        return result
    return wrapper


@cache_results
def multiply(a, b):
    return a * b


print(multiply(12, 5))
print(multiply(12, 9))
