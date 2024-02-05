import asyncio
import sys

async def co1():
    while True:
        print("Co 1")
        await asyncio.sleep(0)  # Adjust sleep time as needed

async def co2():
    while True:
        print("Co 2")
        await asyncio.sleep(0)  # Adjust sleep time as needed

async def co3():
    while True:
        print("Co 3")
        await asyncio.sleep(0)  # Adjust sleep time as needed

async def main():
    task1 = asyncio.create_task(co1())
    task2 = asyncio.create_task(co2())
    task3 = asyncio.create_task(co3())

    try:
        await asyncio.gather(task1, task2, task3)
    except KeyboardInterrupt:
        print("Shutdown signal received. Cancelling tasks...")
        task1.cancel()
        task2.cancel()
        task3.cancel()
        await asyncio.gather(task1, task2, task3, return_exceptions=True)
        print("All tasks completed.")
    finally:
        print("Program exiting...")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # Handle any cleanup here if necessary
        print("Program interrupted by user. Exiting cleanly...")
