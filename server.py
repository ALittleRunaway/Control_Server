from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
import logging

logging.basicConfig(format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG, filemode='a', filename="logs.txt")
logging.info("Running Urban Planning")
logger = logging.getLogger(__name__)
app = FastAPI()


@app.get("/control_state")
async def root(msg: Optional[str] = None):
    if msg:
        logger.debug(msg)
    return FileResponse("logs.txt")


if __name__ == '__main__':
    uvicorn.run("server:app", host="0.0.0.0", port=7777)
