from fastapi import FastAPI
from data import CheckpointPack

app = FastAPI()


@app.get("/")
async def root():
    return


@app.post("/checkpoint/")
async def checkpoint(pack: CheckpointPack):
    print(pack.tester)
    print(pack.map)
    print(pack.checkpoint)
    print(pack.startTime)
    print(len(pack.data), "datapoints")
    return
