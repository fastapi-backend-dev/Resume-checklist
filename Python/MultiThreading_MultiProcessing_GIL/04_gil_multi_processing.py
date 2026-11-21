# `Process` lets this script create separate Python processes.
# Unlike threads, each process has its own Python interpreter and memory.
from multiprocessing import Process

# `time` is used to measure how long both counting processes take together.
import time


def crunch_number():
    """
    This function is the work performed inside one child process.

    Every process runs this function independently and performs the CPU-heavy
    counting job shown below.
    """

    # This message proves that a child process started the function.
    print("Started the count process...")

    # Line 7: Start the counter with a value of zero.
    # This is a local variable inside this process, so it is separate from
    # the variable used by every other process.
    count = 0

    # Line 8: Repeat the next indented line 100 million times.
    # `range(100_000_000)` produces numbers from 0 through 99,999,999.
    # `_` is used as the loop variable because its value is not needed inside
    # the loop; `_` simply makes the loop run the required number of times.
    for _ in range(100_000_000):
        # Line 9: Increase `count` by 1.
        # `count += 1` is the short form of `count = count + 1`.
        # Because this line executes 100 million times, it is a CPU-heavy task.
        count += 1

    # Print a message after this process has finished counting.
    print("Ended the count process...")


# This block runs only when the file is executed directly.
#
# On Windows, each child process imports the main script again. This guard
# prevents the new process from creating the same process objects and starting
# an endless loop of new child processes. Put process creation and starting
# code inside this block for a safe Windows program.
if __name__ == "__main__":
    # Record the start time immediately before the two processes are started.
    start = time.time()

    # Create two process objects. `target=crunch_number` tells each process
    # which function it should execute. The function is not called here with
    # parentheses; `Process` calls it later after `start()` is used.
    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    # Start each child process. The operating system gives each process its
    # own memory and Python interpreter, so both counting jobs can run at the
    # same time on separate CPU cores.
    p1.start()
    p2.start()

    # `join()` makes the main process wait until the specified child finishes.
    # `p1.join()` waits for the first process, and `p2.join()` waits for the
    # second process. It prevents the timing and final print from running too
    # early.
    p1.join()
    p2.join()

    # Record the time after both child processes have finished.
    end = time.time()

    # Calculate the total elapsed time in seconds.
    diff = end - start

    # Print the elapsed time with exactly three digits after the decimal point.
    print(f"Total time taken: {diff:.3f} seconds...")
