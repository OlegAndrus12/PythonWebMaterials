# We say that an object is an awaitable object if it can be used in an await expression. 
# Many asyncio APIs are designed to accept awaitables.
#There are three main types of awaitable objects: coroutines, Tasks, and Futures.


import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())