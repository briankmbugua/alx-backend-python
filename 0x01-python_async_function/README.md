# asyncio
provides a framework for writting asynchronous, concurrent, and parallel code.
- `aysncio.run(main, * , debug=False)`:This is the entry point to running asynchronous code.It takes a coroutine `main` as an argument and executes it.The `debug` parameter can be set to `True` for debugging purposes.
- `asyncio.create_task(coro, *, name=None)`: This method creates a task to run the given coroutine coro. Tasks are used to execute asynchronous functions concurrently.
- `asyncio.ensure_future(coro, *, loop=None)`: Similar to create_task, this method ensures that a coroutine coro is scheduled for execution. You can also specify a custom event loop using the loop parameter.
- `asyncio.sleep(delay, result=None, *, loop=None)`: This method creates a coroutine that suspends its execution for the specified delay in seconds. You can provide an optional result that the coroutine will return when it completes.
- `asyncio.wait_for(coro, timeout, *, loop=None)`: This method waits for the specified coroutine coro to complete or raises a asyncio.TimeoutError if it doesn't complete within the specified timeout.
- `asyncio.gather(*coros, loop=None, return_exceptions=False)`: This function gathers multiple coroutines and runs them concurrently. It returns a list of results from the coroutines, and if return_exceptions is set to True, it won't raise exceptions but include them in the result list.
- `asyncio.shield(coro)`: This method is used to protect a coroutine from being canceled. It returns a new coroutine that wraps the original coroutine coro.
- `asyncio.open_connection(host=None, port=None, *, loop=None, limit=None, **kwds)`: It creates a connection to a remote server. This is often used for network communication and returns a pair of reader and writer objects.
- `asyncio.start_server(client_connected_cb, host=None, port=None, *, loop=None, limit=None, **kwds)`: This method starts a socket server and calls the client_connected_cb coroutine for each incoming client connection.
- `asyncio.Lock()`: This is not a method but a class to create locks for synchronizing access to shared resources in asynchronous code.
- `asyncio.Queue(maxsize=0)`: Another class, this creates a queue used for communication between asynchronous tasks.
- `asyncio.Semaphore(value=1)`: This class represents a semaphore that can be used to control access to a limited number of resources in an asynchronous environment.
