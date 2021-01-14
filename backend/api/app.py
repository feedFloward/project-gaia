from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from .models import ClassificationRequest
from backend.classification.clf_selection import get_model_type

app = FastAPI()

# CORS
origins = [
    'https://localhost:8080',
    'http://192.168.178.24:8080',
    'http://192.168.178.24:8081',
    
    # production
    'http://192.168.235.161:5000'
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
    clf = get_model_type(clf_request)
    response = clf.main()
    return JSONResponse({"answer": response})