from multiprocessing import Process
import time


def brew_chai(name):
    # Simulate brewing this maker's chai for two seconds.
    print(f"Start of {name} brewing...")
    time.sleep(2)
    print(f"End of {name} brewing...")
     

# Run this setup only when the file is launched directly, not when imported.
# On Windows, child processes import this file; this guard prevents them from
# starting the same processes again.
if __name__ == "__main__":
    # Create one process per maker and pass its name to the brewing function.
    # The comma makes args a one-item tuple, as Process expects.
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i}",))
        for i in range(1, 6)
    ]

    # Start all five brewing processes.
    for p in chai_makers:
        p.start()

    # Wait for every process to finish before announcing that chai is served.
    for p in chai_makers:
        p.join()

    print("All chai served...")
