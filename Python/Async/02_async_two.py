"""
time.sleep() VS asyncio.sleep()

time.sleep(3) is a blocking sleep:
    It pauses the whole Python thread for three seconds. If three brewing
    coroutines used time.sleep(3), the first one would block the event loop,
    and the other coroutines could not run during that time.

asyncio.sleep(3) is an asynchronous sleep:
    It pauses only the current coroutine for three seconds and tells the
    event loop that this task is waiting. The event loop can run another
    coroutine during this period. This is useful for concurrent I/O-style
    tasks that spend time waiting.

WHY await IS USED WITH asyncio.sleep()

asyncio.sleep(3) creates an awaitable coroutine, but it does not perform
the sleep simply when it is called. await tells Python to schedule that
waiting operation and pause the current coroutine until it finishes.

Async functions do not run immediately when called. For example:

    brew("Masala Chai")

creates a coroutine object. Calling brew() inside asyncio.gather() is enough
for gather to schedule it, and await is used on gather because gather itself
is an asynchronous operation that we need to wait for.

EASY ANALOGY FOR asyncio.gather()

Imagine you place four kettles on a stove at the same time and ask:
"Please tell me when all four kettles are ready." asyncio.gather() is like
the person waiting for every brewing task to finish. It:

1. Starts (schedules) every coroutine passed to it.
2. Runs the coroutines concurrently on the same event loop.
3. Waits until every coroutine has completed.
4. Returns control back to main() after all tasks finish.

"Concurrent" means the tasks make progress during one another's waiting
period. It does not mean each task runs on a separate CPU core. All four
tasks here wait for the same three-second asyncio.sleep(), so the total time
is approximately three seconds rather than four separate three-second waits.
"""

# asyncio provides the event loop and tools for defining, scheduling, and
# coordinating asynchronous tasks.
import asyncio

# time is imported here only to explain the difference between blocking sleep
# and asynchronous sleep. The program itself uses asyncio.sleep().
import time


# The async keyword means that brew is a coroutine function.
# The name parameter allows us to create a separate brewing task for each tea.
async def brew(name):
    # This line runs immediately when this coroutine begins execution.
    print(f"Start brewing {name}...")

    # asyncio.sleep(3) creates an asynchronous waiting operation.
    # await pauses only this brew coroutine for approximately three seconds.
    #
    # time.sleep(3) would instead block the entire event loop. The commented
    # line below shows that alternative, but it would prevent other brew
    # coroutines and main() from making progress during the delay.
    await asyncio.sleep(3)
    # time.sleep(3)

    # This line runs after this particular brew coroutine finishes sleeping.
    print(f"{name} is ready!!")


# main() is also a coroutine because it may need to wait for gather().
async def main():
    # await means: "Run this asynchronous operation, and resume main() only
    # after gather() has finished waiting for every brewing coroutine."
    await asyncio.gather(
        brew("Masala Chai"),  # First brewing coroutine
        brew("Green Tea"),    # Second brewing coroutine
        brew("Ginger Chai"),  # Third brewing coroutine
        brew("Elaichi Chai")  # Fourth brewing coroutine
    )

    # Because gather() waited for all coroutines, this message would run only
    # after every tea has reached the print statement that says it is ready.


# This synchronous-looking entry point calls asyncio.run(), which creates and
# starts the event loop, schedules main(), and waits until main() and all of
# the tasks started by main() are complete.
asyncio.run(main())
