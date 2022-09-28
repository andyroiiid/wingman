import os

from fastapi import FastAPI
from data import CheckpointPack
from time import gmtime
from base64 import standard_b64decode

app = FastAPI()


@app.get("/")
async def root():
    return


@app.post("/checkpoint/")
async def checkpoint(pack: CheckpointPack):
    gmt = gmtime()
    timestamp = f"{gmt.tm_year:04}{gmt.tm_mon:02}{gmt.tm_mday:02}{gmt.tm_hour:02}{gmt.tm_min:02}{gmt.tm_sec:02}"
    os.makedirs(f"data/{pack.map}", exist_ok=True)
    with open(f"data/{pack.map}/{pack.tester}_{timestamp}.bin", "wb") as f:
        f.write(standard_b64decode(pack.movement))
    return
