from fastapi import FastAPI, Response
import json

app = FastAPI()

@app.get("/")
def get_items():
    data = json.dumps({"data":"Hello World"})
    return Response(content=data, media_type="application/json")