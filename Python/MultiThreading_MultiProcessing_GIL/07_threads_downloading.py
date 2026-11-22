# Threading is useful here because downloading files spends most of its time
# waiting for network responses, not performing CPU-heavy work. Instead of
# waiting for one download to finish before starting the next, Python can start
# multiple threads and let them wait in parallel. While one thread waits for
# httpbin.org, another thread can send and receive its own request. This reduces
# the total waiting time and makes better use of the available network connection.
# Joining each thread ensures the program waits for every download to complete.

import threading
import requests
import time


def download_image(url):
    # Send the network request and report the downloaded response size.
    print(f"Started downloading from {url}...")
    response = requests.get(url)
    print(f"Finished downloading from url: {url}, sie: {len(response.content)} bytes.")


# Multiple URLs allow several download operations to run concurrently.
urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]
# Keep thread objects so they can be joined after all downloads start.
threads = []

# Measure total elapsed time for the download batch.
start = time.time()

# Start one thread for every image URL.
for url in urls:
    t = threading.Thread(target=download_image, args=(url,))
    t.start()
    threads.append(t)

# Wait for each download thread to finish before the program exits.
for t in threads:
    t.join()

# Report the combined download time.
end = time.time()
diff = end - start
print(f"All images downloaded in {diff:.3f} seconds")
