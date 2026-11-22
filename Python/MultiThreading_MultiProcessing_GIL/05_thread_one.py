import threading
import time


def boil_milk():
    # Simulate a 2-second milk-boiling task.
    print("Boiling milk...")
    time.sleep(2)
    print("Boiled milk...")


def toast_bun():
    # Simulate a 3-second bun-toasting task.
    print("Toasting bun...")
    time.sleep(3)
    print("Done with bun toast...")


# Measure elapsed time for both concurrent tasks.
start = time.time()

# Create independent threads for the breakfast tasks.
t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

# Start both tasks concurrently.
t1.start()
t2.start()

# Wait until both threads finish.
t1.join()
t2.join()

end = time.time()
diff = end - start
print(f"Breakfast ready in {diff:.3f} seconds")
