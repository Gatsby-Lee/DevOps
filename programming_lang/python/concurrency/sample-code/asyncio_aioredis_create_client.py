"""
@ref: https://github.com/aio-libs/aioredis
"""
import os
import asyncio

import aioredis

REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None)
REDIS_CLIENT = []

async def get_async_redis_cliet():

    try:
        return REDIS_CLIENT[0]
    except Exception:
        redis_info = {
            'address': (REDIS_HOST, REDIS_PORT),
            'password': REDIS_PASSWORD
        }
        coroutine_obj = aioredis.create_redis(**redis_info)
        async_redis_client = await coroutine_obj
        REDIS_CLIENT.append(async_redis_client)
        return REDIS_CLIENT[0]


async def main():
    async_redis_client = await get_async_redis_cliet()
    print(async_redis_client)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
