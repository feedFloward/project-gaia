from typing import List, Dict
from pydantic import BaseModel, Field


class ClassObject(BaseModel):
    index: int
    points: List[List[float]]
    color: str


class InputspaceClass(BaseModel):
    inputspaceHeight: int
    inputspaceWidth: int


class ModelObject(BaseModel):
    text: str
    value: str
    specs: Dict


class TrainSpecObject(BaseModel):
    testSize: float


class ClassificationRequest(BaseModel):
    data: List[ClassObject]
    inputspace: InputspaceClass
    model: ModelObject
    train_specs: TrainSpecObject