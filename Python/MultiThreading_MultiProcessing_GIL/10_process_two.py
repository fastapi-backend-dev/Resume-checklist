# Multiprocessing is useful here because cpu_heavy() performs a long,
# CPU-intensive calculation. Each process runs in a separate Python interpreter
# and has its own GIL, so the calculation can run on multiple CPU cores instead
# of being limited to one core by threading. The two processes work independently
# and do not compete to update shared Python data. Process creation has some
# overhead, so it works best when the calculation is large compared with that
# overhead. In this example, both processes repeat the same calculation; the
# efficiency would be even greater if the loop were split into different ranges
# and the partial results were combined later.

from multiprocessing import Process
import time


def cpu_heavy():
    # Run the same CPU-heavy loop in each process.
    print("Crunching some numbers...")
    total = 0
    for i in range(10**9):
        total += i
    print("Done ✔️")


# Protect process creation on Windows and other platforms.
if __name__ == "__main__":
    # Measure the time taken by all processes.
    start = time.time()

    # Create two processes that each execute the entire calculation.
    processes = [Process(target=cpu_heavy) for _ in range(2)]

    # Start the processes and wait for both to finish.
    [p.start() for p in processes]
    [p.join() for p in processes]

    end = time.time()
    diff = end - start
    print(f"Total time taken: {diff:.3f} seconds")
