# A lock prevents several threads from changing the same data at the same time.
# Here, counter += 1 is a shared operation that can be interrupted by another
# thread. The lock gives one thread exclusive access to the operation until it
# finishes. We use "with lock:" because it automatically acquires the lock before
# entering the block and releases it afterward, even if an error occurs.
# This keeps the final counter value equal to 10 x 100,000 = 1,000,000.

import threading
import time

counter = 0
lock = threading.Lock()


def increment():
    # Only one thread can update counter at a time.
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1


# Create 10 threads that each increment counter 100,000 times.
threads = [threading.Thread(target=increment) for _ in range(10)]

# Start all threads, then wait for every thread to finish.
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final value: {counter}")
