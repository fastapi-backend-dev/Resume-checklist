"""
AIOHTTP - SIMPLE EXPLANATION

aiohttp is a third-party Python library for making and receiving HTTP requests
without blocking the event loop. It is useful for async work such as downloading
several web pages or calling several APIs at the same time.

ANALOGY

Think of aiohttp as an async internet assistant. A ClientSession is the
assistant's reusable phone line. session.get(url) asks for a web page. async
with is a safe "open now, clean up automatically later" block.

ClientSession

aiohttp.ClientSession() creates an HTTP session. The session keeps connection
information and a connection pool, so several requests can reuse resources.
Creating one session for many requests is more efficient than creating a
separate session for every request.

async with

An async with block is the asynchronous version of a normal with block.
It calls setup logic, runs the indented code, and calls cleanup logic when
the block finishes. It is usually used for resources that need opening and
closing, such as a ClientSession or an HTTP response.

session.get(url)

session.get(url) starts an HTTP GET request. It is both an awaitable request
and an asynchronous context manager here. async with session.get(url) as
response first waits for the response headers, gives that response to
response, and closes/releases the response when the block ends.

aiohttp.ClientSession()

aiohttp.ClientSession() is a session factory. It normally creates a
TCPConnector that verifies HTTPS certificates. A connector is the part that
opens network connections and manages SSL/TLS verification.

WHY THE CURRENT CODE CAN GIVE AN SSL ERROR

This code asks for https://httpbin.org/delay/3. The HTTPS connection requires
certificate verification. In this environment, aiohttp can raise
SSLCertVerificationError when it cannot verify httpbin.org's certificate.
For example, the server, proxy, certificate store, or machine clock may cause
the certificate to be treated as expired or untrusted.

THE COMMENTED ssl=False CODE

TCPConnector(ssl=False) creates a connector that disables certificate
verification for this HTTPS connection:

    connector = aiohttp.TCPConnector(ssl=False)
    async with aiohttp.ClientSession(connector=connector) as session:

This may avoid the certificate error, which is why the run can appear to work
when the commented code is used. However, ssl=False does not verify the
server's identity. It is unsafe for real applications because a fake server,
proxy, or man-in-the-middle may be trusted.

For real programs, normally keep verification enabled and fix the root issue:
the certificate, certificate store, proxy settings, system clock, or trusted
CA configuration.
"""

# asyncio provides the event loop and helpers such as gather().
import asyncio

# aiohttp provides the async HTTP ClientSession and HTTP request tools.
import aiohttp


# fetch_url is a coroutine for downloading/reading one URL.
# session is reused for all URLs so the requests share one connection pool.
# aiohttp.ClientSession is the type used for the session parameter.
async def fetch_url(session: aiohttp.ClientSession, url):
    # session.get(url) creates and starts the HTTP GET operation.
    # async with awaits the response and then manages response cleanup.
    # "as response" gives the received HTTP response object the name response.
    async with session.get(url) as response:
        # response.status contains the HTTP status code, such as 200 or 404.
        print(f"Fetched {url} with status code of {response.status}")


async def main():
    # Create a list containing the same slow endpoint three times.
    # The endpoint delays its response for approximately three seconds.
    urls = ["https://httpbin.org/delay/3"] * 3

    # Optional workaround code:
    # connector = aiohttp.TCPConnector(ssl=False)
    #
    # This passes the non-verifying connector into the session:
    # async with aiohttp.ClientSession(connector=connector) as session:

    # Opening this session is an async setup step. The indented code can use
    # the session, and it is closed automatically when this block exits.
    async with aiohttp.ClientSession() as session:
        # Create one coroutine object for every URL. Calling fetch_url() does
        # not execute the network request immediately; gather() schedules it.
        tasks = [fetch_url(session, url) for url in urls]

        # gather() starts all tasks together and await waits for every request
        # to finish. It is similar to placing three calls on hold and waiting
        # until all three assistants report back.
        await asyncio.gather(*tasks)


# asyncio.run() creates and starts the event loop, runs main(), and closes the
# loop after main() and all gathered tasks have completed.
asyncio.run(main())
