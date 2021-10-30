import asyncio
import time


async def worker():
    print('worker - will take some time')
    time.sleep(3)
    print('worker - done it')
    return 42


async def do_something():
    print('do_something - will wait for worker')
    result = await worker()
    print('do_something - result:', result)


def main():
    print('Main - Starting')
    asyncio.run(do_something())
    print('Main - Done')


if __name__ == '__main__':
    main()