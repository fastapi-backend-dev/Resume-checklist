# threading lets us run multiple tasks in the same Python process.
# Here it is used to create two workers that do a CPU-heavy counting job.
import threading

# time is used to measure how many seconds the complete operation takes.
import time


def brew_chai():
    """
    This function represents one chai-making worker.

    Each thread receives this same function as its task. Both threads run
    the function separately, and each one uses its own local `count` value.
    """

    # Show which worker started. `current_thread().name` gives the thread's
    # custom name, such as "Barista-1" or "Barista-2".
    print(f"{threading.current_thread().name} started brewing...")

    # This variable is local to the function. Every call of brew_chai has
    # a separate count value, so thread 1 and thread 2 do not share it.
    count = 0

    # This is the CPU-heavy part of the script.
    # - `range(100_000_000)` creates a sequence from 0 to 99,999,999.
    # - `_` is used as the loop variable because the actual number is not
    #   needed inside the loop; it simply controls how many times the loop runs.
    # - `count += 1` means `count = count + 1`. It executes 100 million times.
    #   This repeated addition keeps the CPU busy and helps demonstrate the
    #   Global Interpreter Lock (GIL) behavior of Python threads.
    for _ in range(100_000_000):
        count += 1

    # Display the thread that finished its counting work.
    print(f"{threading.current_thread().name} finished brewing...")


# Create the first thread. `target` is the function that the thread will run,
# and `name` makes this worker easy to identify in the printed output.
thread1 = threading.Thread(target=brew_chai, name="Barista-1")

# Create the second thread. Both threads run the same `brew_chai` function.
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

# Record the starting time just before the workers begin.
start = time.time()

# `start()` tells a thread to begin running the `target` function.
# Both calls are made quickly, so both workers are ready to do the counting.
thread1.start()
thread2.start()

# `join()` makes the main program wait here until the specified thread ends.
# - After `thread1.join()`, the main thread waits for Barista-1.
# - After `thread2.join()`, it also waits for Barista-2.
# Without join(), the next timing code could run before the workers finish.
thread1.join()
thread2.join()

# Record the time after both worker threads have finished.
end = time.time()

# Calculate the total running time.
diff = end - start

# Print the result with exactly three digits after the decimal point.
print(f"Total time taken: {diff:.3f} seconds...")
