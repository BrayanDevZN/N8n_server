from src.config.settings import ENVIRONMENT
from src.redis.control import logger, client
from src.storage.file import block

from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware

class Midlleware(BaseHTTPMiddleware):

    @staticmethod
    async def _global() -> None:

        limit = ENVIRONMENT["global_rate_limit"]

        number = await client.get(name="global_rate_limit")

        if number is not None and int(number) > (limit):

            raise HTTPException(
                status_code=429,
                detail="Exeded global rate limit"
            )

        await client.incr(name="global_rate_limit")


    async def _limit(self, request:Request) -> None:

        limit = ENVIRONMENT["rate_limit"]

        user = request.client.host 

        name = f"rate_limit:{user}"

        number = await client.get(name)

        if number is not None and int(number)>int(limit):

            msg  = f"Exceded rate limit for host {user}"

            logger.warning(msg)

            await self._set_block(request)

            raise HTTPException(
                detail=msg, 
                status_code=429
            )


        await client.incr(name)

    @staticmethod
    async def _set_block(request:Request) -> None:

        if ENVIRONMENT["block"]:

            user = request.client.host

            data = await block.read()

            data[user] = data[user] + 1 if data and  user in data.keys()  else 1

            await block.save(data)

    @staticmethod
    async def _block(request:Request) -> None:

            if ENVIRONMENT["block"]:

                user = request.client.host

                data = await block.read()

                if data and user in data.keys() and data[user] > ENVIRONMENT["block_limit"]:
                    msg = f"user {user} bloqued"

                    logger.warning(msg)

                    raise HTTPException(
                        status_code=401,
                        detail=msg
                    )


    async def dispatch(self, request:Request, call_next):

        if ENVIRONMENT["environment"] == "prod":

            await self._block(request=request)
            await self._global()
            await self._limit(request=request)


        return await call_next(request)
        



        

    

