# This won't run on Windows, as signal handling is not supported on Windows.    
import asyncio
import signal

shutdown_requested = False

def signal_handler():
    global shutdown_requested
    print("Shutdown signal received.")
    shutdown_requested = True

async def co1():
    while not shutdown_requested:
        print("coroutine 1")
        await asyncio.sleep(0)  # Yield control

async def co2():
    while not shutdown_requested:
        print("Coroutine 2")
        await asyncio.sleep(0)  # Yield control

async def co3():
    while not shutdown_requested:
        print("Co 3")
        await asyncio.sleep(0)  # Yield control

async def main():
    # Register the signal handler for SIGINT
    loop = asyncio.get_running_loop()
    loop.add_signal_handler(signal.SIGINT, signal_handler)

    task1 = asyncio.create_task(co1())
    task2 = asyncio.create_task(co2())
    task3 = asyncio.create_task(co3())

    # Wait for all tasks to complete (they won't without external intervention)
    await asyncio.gather(task1, task2, task3, return_exceptions=True)
    print("All tasks completed.")

if __name__ == "__main__":
    asyncio.run(main())
    print("Program exited cleanly.")
