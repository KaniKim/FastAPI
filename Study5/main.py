import random
import uuid
import contextvars
from loguru import logger
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

request_id_contextvar = contextvars.ContextVar("request_id", default=None)


def divide(a, b):
    print(f"Dividing {a} / {b} ... ")
    result = a / b
    print(f"Result is {result}")


@app.middleware("http")
async def request_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request_id_contextvar.set(request_id)
    logger.debug("Request Started")

    try:
        return await call_next(request)

    except Exception as e:
        logger.debug(f"Request failed: {e}")
        return JSONResponse(content={"Success": False}, status_code=500)

    finally:
        assert request_id_contextvar.get() == request_id
        logger.debug("Request ended")


@app.get("/")
def read_root():
    a = 100
    b = random.randint(0, 1)
    return {"success": True, "resut": divide(a, b)}
