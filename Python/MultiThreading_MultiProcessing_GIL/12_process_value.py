# Value creates a small piece of shared memory that can be accessed by multiple
# processes. Normal Python variables are not shared between processes; each
# process normally gets its own separate copy. The shared memory object returned
# by Value lets processes communicate and update the same integer or other data.
# .get_lock() returns the lock associated with this shared value. The lock ensures
# that only one process changes the value at a time, preventing lost updates.
# "with counter.get_lock()" automatically acquires the lock before entering the
# block and releases it afterward.
# .value reads or updates the actual data stored inside the shared memory object.

from multiprocessing import Process, Value


def increment(counter):
    # Each process repeats the increment operation 100,000 times.
    for _ in range(100_000):
        # Only one process may enter this block at a time.
        with counter.get_lock():
            # Read counter.value, add 1, then store it back in shared memory.
            counter.value += 1


if __name__ == "__main__":
    # "i" means a signed integer, and 0 is the starting shared value.
    counter = Value("i", 0)

    # Create four separate processes, all using the same shared counter.
    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]

    # Start all processes and wait until every process has finished.
    [p.start() for p in processes]
    [p.join() for p in processes]

    # Read the final shared value after all 400,000 increments finish.
    print(f"Final value of counter: {counter.value}")
