# A multiprocessing Queue lets separate processes exchange information safely.
# Each process has its own memory, so a normal variable in the child process is
# not automatically updated in the parent process. A Queue acts like a shared
# communication channel: the child puts a value into the Queue, and the parent
# gets it back. queue.put() sends or adds an item to the Queue, while
# queue.get() receives or removes the next item. Queue is useful for passing
# tasks, results, and messages between processes. queue.get() waits until an
# item is available if the Queue is currently empty.

from multiprocessing import Process, Queue


def prepare_chai(queue: Queue):
    # This function runs inside the child process.
    # put() places the chai message into the Queue for the parent process.
    queue.put("Masala Chai is ready...")


if __name__ == "__main__":
    # Create the communication Queue in the parent process.
    queue = Queue()

    # Pass the Queue to the child process as an argument.
    p = Process(target=prepare_chai, args=(queue,))

    # Start the child process so it can run prepare_chai().
    p.start()

    # Wait here until the child process finishes sending the message.
    p.join()

    # get() retrieves the message sent through the Queue.
    # Communication is happening between processes: child -> Queue -> parent.
    print(queue.get())
