from threading import Thread
import time


def order_chai():
    # Handle five chai orders, pausing briefly between each one.
    for i in range(1, 6):
        print(f"Chai Order #{i}")
        time.sleep(1)


def brew_chai():
    # Brew five cups; this takes longer than handling the orders.
    for i in range(1, 6):
        print(f"Chai Brew #{i}")
        time.sleep(2)


# Give each task its own thread so they can run at the same time.
order_thread = Thread(target=order_chai)
brew_thread = Thread(target=brew_chai)

# start() begins each task on its thread.
order_thread.start()
brew_thread.start()

# Wait for both tasks to finish before the main thread continues.
# Without join(), code after these calls could run while a task is still working.
# join() makes the main thread wait until each worker finishes, so later code won’t run while those tasks are still working.
order_thread.join()
brew_thread.join()
