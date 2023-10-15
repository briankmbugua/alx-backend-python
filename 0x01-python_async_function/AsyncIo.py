"""
What asynchronous I/O is not
not mutlithreading
not multiprocessing
it is concurrency
concurrency is when two or more tasks can start, run, and complete in overlapping time periods
#example:
func1()
func2()
func3()
if synchronous, func2() will not start until func1() finishes and so on
If we use multiprocessing or multithreading we would define three different processes or threads in this case, we would run all three functions at the same time or roughly the same time or create an illusion of running at the same time.This is not the goal of asynchronous programming.
What asynchronous programming would do in this case, let's say if func1() dpes something productive like requesting data from a database or it's waiting for something we would not want to waste cpu time and we would go on to execute func2 and func3 and then come back to func1 when it's ready to do something again.
"""
import asyncio

async def main():
    task = asyncio.create_task(other_function())
    print("A")
    await asyncio.sleep(5)
    print("B")
    print(await task)
    # print(f"Return value was {return_value}")

async def other_function():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return 10

asyncio.run(main())
