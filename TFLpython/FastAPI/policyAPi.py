from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="TFLInsurance API", description="Simple Insurance Policy Management REST API", version="1.0")

class Policy(BaseModel):
    name: str
    description : str
    maturity : str
    premium : float

policies = [
    {
        "id:"
    }
]