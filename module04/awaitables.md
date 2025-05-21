| Term          | What it is                                                    | Created with                                       | Used for                                        |
| ------------- | ------------------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------- |
| **Coroutine** | A function you define with `async def`                        | `async def`, returns coroutine object              | Describes *what to do* asynchronously           |
| **Task**      | A wrapper that schedules a coroutine                          | `asyncio.create_task()`                            | Actually *runs* the coroutine in the event loop |
| **Future**    | A low-level object representing a result that’s not ready yet | `asyncio.Future()` (manually or behind the scenes) | Holds the result of an async operation          |
