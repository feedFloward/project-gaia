from typing import List, Dict, Union
from pydantic import BaseModel, Field


class SvmSpecs(BaseModel):
    kernel: str


class RandomForestSpecs(BaseModel):
    numberEstimators: int


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
    specs: Union[SvmSpecs, RandomForestSpecs]


class TrainSpecObject(BaseModel):
    testSize: float


class ClassificationRequest(BaseModel):
    data: List[ClassObject]
    inputspace: InputspaceClass
    model: ModelObject
    train_specs: TrainSpecObject
