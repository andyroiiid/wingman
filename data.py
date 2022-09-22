from typing import List

from pydantic import BaseModel


class Orientation(BaseModel):
    p: float  # pitch
    y: float  # yaw


class Vec3(BaseModel):
    x: float
    y: float
    z: float


class DataPoint(BaseModel):
    t: float  # time
    p: Vec3  # position
    v: Vec3  # velocity
    a: Orientation  # aim


class CheckpointPack(BaseModel):
    tester: str
    map: str
    checkpoint: str
    startTime: float
    data: List[DataPoint]
