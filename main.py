from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
classifier = pipeline("text-classification")



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text )[0]