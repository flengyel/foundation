# FOUNDATION

This repository contains foundational routines in asyncio and Kivy intended 
as building blocks for more complex projects. The examples demonstrate asyncio 
patterns combined with Kivy for GUI applications, with a particular emphasis 
on handling asynchronous tasks and user interfaces.

- `asyncio_cancellable_coroutines.py`: Demonstrates how to implement cancellable coroutines in asyncio, ensuring clean exits across various environments including Windows, WSL2 Ubuntu, and Raspbian. Ideal for tasks requiring graceful shutdowns.

- `asyncio_coroutines.py`: Showcases basic asyncio coroutine usage. While it runs well across platforms, it may not exit as cleanly on Windows, highlighting differences in asyncio behavior across environments.

- `asyncio_coroutines_with_sigint.py`: Explores handling SIGINT signals with asyncio, making it incompatible with Windows due to its different signal handling mechanisms. Useful for understanding asyncio's interaction with system signals on Unix-like systems.



## What is this code for?

In part to understand asyncio, and in part to provide a skeleton for other projects.

The code `asyncio_cancellable_coroutines.py` will be used to integrate Kivy with RYLR998-LoRa. Serial
I/O and command processing (dequeing) will rely on cancellable coroutines.

The Boolean property waitForReply will control when commands are dequeued.

The order of priority is as follows. 

1. The RCV command from the REYAX RYLR998 serial port takes priority over 
2. AT command responses, which take priority over
3. user input, one character at a time (the msg buffer is advances), which takes priority over
4. AT commands, which are dequeued from an asyncio queue, provided waitForReply is False.


