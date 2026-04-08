from fastapi import FastAPI, Body
from environment import SQLEnv

app = FastAPI()
env = SQLEnv()

@app.get("/")
def health(): return {"status": "online"}

@app.post("/reset")
async def reset():
    return {"observation": env.reset()}

@app.post("/step")
async def step(payload: dict = Body(...)):
    action = payload.get("action", "")
    obs, reward, done = env.step(action)
    return {"observation": obs, "reward": reward, "done": done}