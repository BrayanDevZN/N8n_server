from src.redis.connection import conn, logger
from redis import WatchError

class RedisControl:

    async def incr(self, name:str) -> None:

        while True:

            try:

                logger.info(f"Tentando incrementar em {name}...")

                with conn.pipeline(transaction=True) as session:

                    session.watch(name)

                    session.multi()

                    session.incr(name=name)

                    session.expire(time=60, name=name)

                    session.execute()

                    logger.info("Incrementado!!!")

                    break

            except WatchError:

                logger.warning(f"Alguem ja estava modificando chave {name}!!!")

    async def get(self, name:str) -> int|None:


            try:

        

                logger.info(f"Tentando ler {name}...")

                with conn.pipeline() as session:

                    session.get(name=name)

                    result = session.execute()[0]

                logger.info(name + " " +  "não" if result is None else "" + "encontrado!!")

                return result

            except Exception as e:

                logger.error(f"Houve um erro ao ler {name}: {e}")
                raise



client = RedisControl()

    

            

                


        