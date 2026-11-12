def serve_chai():
    yield "A"
    yield "B"
    yield "C"


gen = serve_chai()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))
