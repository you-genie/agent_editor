from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class NodeTestRequest(BaseModel):
    node_id: str
    prompt: str
    input_state: dict
    model: str

@app.get("/")
def read_root():
    return {"status": "ok"}

@app.post("/test_node")
def test_node(req: NodeTestRequest):
    # Placeholder: run the node logic here
    return {"result": f"Tested node {req.node_id} with model {req.model}"} 