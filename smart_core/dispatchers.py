# Dispatcher classes for handling different types of emergencies
# Coroutine handlers for fire, police, medical emergencies

import asyncio
from collections import deque

class Dispatcher:
    def __init__(self, name):
        self.name = name
        self.queue = deque()

    async def run(self):
        while True:
            if self.queue:
                event = self.queue.popleft()
                print(f"[{self.name.upper()}] Processing: {event}")
            await asyncio.sleep(0)  # Yield control