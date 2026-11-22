# Threading is not very useful here because cpu_heavy() performs a CPU-intensive
# calculation instead of waiting for network or file operations. In standard
# CPython, the GIL allows only one thread to execute Python bytecode at a time.
# Therefore, two threads usually do not run this loop in parallel across CPU
# cores, so the work can take nearly the same time as one thread or even more
# due to thread switching. For this kind of task, multiprocessing is usually
# better because each process gets its own Python interpreter and GIL.

import threading
import time


def cpu_heavy():
    # Simulate a CPU-heavy loop that continuously executes Python instructions.
    print("Crunching some numbers...")
    total = 0
    for i in range(10**8):
        total += i
    print("Done ✔️")


# Measure the time taken by the full threaded workload.
start = time.time()

# Create two threads that perform the same CPU-heavy calculation.
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

# Start both threads and wait until both finish.
[t.start() for t in threads]
[t.join() for t in threads]

end = time.time()
diff = end - start
print(f"Total time taken: {diff:.3f} seconds")
