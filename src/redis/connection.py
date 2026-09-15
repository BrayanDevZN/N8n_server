from src.logs.log import logger
from src.config.settings import ENVIRONMENT
from redis import Redis
class ConnectRedisError(Exception):
    pass

logger.info("Criando conexão com redis...")
client = Redis(
    port=6379, 
    host="redis",
    decode_responses=True
)




countdown = 3
while True:

    try:
        logger.info("Testando conexão com redis...")

        client.ping()

        break

    except Exception as e:

        if countdown !=0:
            logger.error(f"houve um erro na conexão com redis: {e}")
            raise

        else:

            logger.warning("Houve um erro, executando teste novamente...")
            countdown -=1
            continue

    

        





