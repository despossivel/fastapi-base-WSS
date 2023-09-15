from fastapi import FastAPI, HTTPException
from src.controllers.demo import controller_demo
from src.controllers.websocket import websocket_endpoint
from starlette.websockets import WebSocket

app = FastAPI()
    
@app.get("/")
@app.get("/demo")
@app.post("/demo")
@app.put("/demo")
@app.delete("/demo")
async def get_demo():
   return controller_demo()

@app.websocket("/ws")
async def websocket_(websocket: WebSocket):
   websocket_endpoint()
