"""
ASYNC/AWAIT - SIMPLE EXPLANATION

async and await allow Python to manage tasks that spend time waiting, such
as a network response or a timer. While one task is waiting, Python may run
another task instead of stopping completely.

The async keyword creates a coroutine function. Calling such a function
does not run it immediately; it creates a coroutine object that can be
scheduled later.

The await keyword pauses the current coroutine only. It does not block the
entire program and gives control back to the event loop while the awaited
operation is waiting. Execution resumes from the same point when it is ready.

asyncio.sleep(seconds):
    An asynchronous replacement for time.sleep(). It tells the event loop,
    "This coroutine has nothing to do for these seconds," so other ready
    tasks can continue during that waiting period.

asyncio.run(coroutine):
    Starts an asyncio event loop, runs the given coroutine, and closes the
    event loop when the coroutine finishes. It is normally used once at the
    entry point of a synchronous Python program.

ASYNC VS. MULTITHREADING VS. MULTIPROCESSING

Async programming:
    Uses one thread and cooperatively switches between tasks while tasks are
    waiting. It works especially well for I/O-bound work, such as web APIs,
    file operations, and database requests.

Multi-threading:
    Uses multiple threads, which can switch on waiting or according to the
    operating system. Python threads are limited for CPU-heavy Python work
    by the Global Interpreter Lock (GIL), but can help with waiting for
    I/O operations.

Multi-processing:
    Uses separate Python processes. It can run CPU-heavy work on multiple
    CPU cores because processes are not restricted by the same GIL as threads.
    Processes are useful for parallel computations but cost more to start
    and are more complex to coordinate.
"""

# The asyncio module provides the event loop, coroutine support, and
# asynchronous functions such as asyncio.sleep().
import asyncio


# This function is a coroutine because it uses the async keyword.
async def brew_chai():
    # Print a message immediately when this coroutine starts.
    print("Start brewing chai...")

    # Wait asynchronously for three seconds. Instead of blocking the whole
    # program, await gives control to the event loop during the delay.
    # When the delay finishes, this function resumes at the next line.
    await asyncio.sleep(3)

    # This runs after the await operation is complete.
    print("Chai is ready!!")


# Calling brew_chai() alone would only create a coroutine object.
# asyncio.run() starts the event loop, schedules brew_chai(), waits for it
# to finish, and then closes the event loop.
asyncio.run(brew_chai())
