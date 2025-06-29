import asyncio
import threading
from app.state import scheduler, dispatchers

def run_backend():
    async def start():
        await asyncio.gather(
            *(d.run() for d in dispatchers.values()),
            scheduler.run()
        )

    loop = asyncio.new_event_loop()
    threading.Thread(target=loop.run_until_complete, args=(start(),), daemon=True).start()