"""To execute an async function, we need an event loop.
And run your asynchronous funcions inside it."""


# Importing the asyncio module
import asyncio


# Defining an async function
async def coroutineOne():
    await asyncio.sleep(5)
    print("coroutineOne is active on the event loop")

# Create an event loop using asyncio.get-event_loop()
loop = asyncio.get_event_loop()

""" Schedule a coroutine or async function to to run within the
event loop using loop.run_until_complete()"""


result = loop.run_until_complete(coroutineOne())


"""you can schedule multiple coroutines to run within the event loop
using asynciogather()"""


async def coroutineTwo():
    await asyncio.sleep(2)
    print("coroutineTwo is active on the event loop")


results = loop.run_until_complete(
    asyncio.gather(coroutineOne(), coroutineTwo())
    )


# close the event loop when you are done with it
loop.close()
