# FOUNDATION

Some asyncio and kivy foundational routines for other projects.

- `asyncio_cancellable_coroutines.py` runs well and exits cleanly under Windows, WSL2 Ubuntu, and Raspian.

- `asyncio_coroutines.py` runs well, but doesn't exit as cleanly under Windows as the previous code.

- `asyncio_coroutines_with_sigint.py` is incompatible with Windows, which does not support signal.

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

## Why make a repository out of it?

I felt like it. I didn't want the code to get lost.

## Why mention other projects? Shouldn't the code be self-contained?

Go fork yourself a copy of the repository and remove whatever you desire.
