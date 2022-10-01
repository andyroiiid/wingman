from pydantic import BaseModel


class CheckpointPack(BaseModel):
    tester: str
    map: str
    checkpoint: str
    time: float
    movement: str
