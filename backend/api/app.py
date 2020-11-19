from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .models import ClassificationRequest
from ..classification.classifier import SOME_CONST

print(SOME_CONST)

app = FastAPI()

# CORS
origins = [
    'https://localhost:8080',
    'http://192.168.178.24:8080',
    'http://192.168.178.24:8081'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

URL_BASE = "/api/v0.1"


@app.post(URL_BASE+"/classification")
async def classification(clf_request: ClassificationRequest):
    print(clf_request.data[0].points)
    return JSONResponse({"answer": "yes"})