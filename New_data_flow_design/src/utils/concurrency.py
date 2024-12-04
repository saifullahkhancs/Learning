import typing
import asyncio
import functools
import contextvars

T = typing.TypeVar("T")


async def run_in_threadpool(
        func: typing.Callable[..., T], *args: typing.Any, **kwargs: typing.Any
) -> T:
    loop = asyncio.get_event_loop()
    child = functools.partial(func, *args, **kwargs)
    context = contextvars.copy_context()
    func = context.run
    args = (child,)
    return await loop.run_in_executor(None, func, *args)


def run_as_async(f):
    async def decorator(*args, **kwargs):
        return await run_in_threadpool(f, *args, **kwargs)

    return decorator
