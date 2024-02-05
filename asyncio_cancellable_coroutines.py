import asyncio

async def cancellable_task_1():
    try:
        while True:
            print("Running task 1...")
            await asyncio.sleep(0)  # Use a small delay to prevent hogging the CPU
    except asyncio.CancelledError:
        print("Task 1 was cancelled!")
        # Perform any necessary cleanup here
    finally:
        print("Cleanup for task 1 complete.")

async def cancellable_task_2():
    try:
        while True:
            print("Running task 2...")
            await asyncio.sleep(0)  # Use a small delay to prevent hogging the CPU
    except asyncio.CancelledError:
        print("Task 2 was cancelled!")
        # Perform any necessary cleanup here
    finally:
        print("Cleanup for task 2 complete.")

async def cancellable_task_3():
    try:
        while True:
            print("Running task 3...")
            await asyncio.sleep(0)  # Use a small delay to prevent hogging the CPU
    except asyncio.CancelledError:
        print("Task 3 was cancelled!")
        # Perform any necessary cleanup here
    finally:
        print("Cleanup for task 3 complete.")

async def main():
    tasks = [
        asyncio.create_task(cancellable_task_1()),
        asyncio.create_task(cancellable_task_2()),
        asyncio.create_task(cancellable_task_3()),
    ]

    try:
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        print("Shutdown signal received. Cancelling tasks...")
        for task in tasks:
            task.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
        print("All tasks have been cancelled and cleaned up.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        # redundant for handling KeyboardInterrupt but ensures a clean exit
        print("Program terminated cleanly.")

