from fastapi import FastAPI
from data import CheckpointPack
from time import gmtime
import json

app = FastAPI()


@app.get("/")
async def root():
    return


@app.post("/checkpoint/")
async def checkpoint(pack: CheckpointPack):
    gmt = gmtime()
    timestamp = f"{gmt.tm_year}_{gmt.tm_mon}_{gmt.tm_mday}_{gmt.tm_hour}_{gmt.tm_min}_{gmt.tm_sec}_{pack.tester}"
    with open(timestamp, "w") as f:
        json.dump(pack.dict(), f)
    return
