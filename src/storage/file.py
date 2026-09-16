import json
from src.logs.log import logger
from pathlib import Path
import os
class BlockControl:

    def __init__(self)-> None:

        self.BASE_DIR = Path(__file__).resolve().parent / "block.json"


    def _exists(self) -> None:

        if not os.path.exists(self.BASE_DIR):

            raise FileNotFoundError(f"Not found file in {self.BASE_DIR}")


    async def read(self) -> dict:

        self._exists()

        with open(self.BASE_DIR, "r") as file:

            file = json.load(file)
            return file if file is not None else {}


    async def save(self) -> None:

        self._exists()

        with open(self.BASE_DIR, "w", encoding="utf-8") as file:

            file = json.dumps(self.BASE_DIR, file, ensure_ascii=False, indent=4)
        


block = BlockControl()


    

        


        


        

    