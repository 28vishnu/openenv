import uvicorn
from fastapi import FastAPI, Body, Request
from .environment import SQLEnv  # Note the DOT before environment

app = FastAPI()
env = SQLEnv()

@app.get("/")
def health(): return {"status": "online"}

@app.post("/reset")
async def reset(request: Request):
    return {"observation": env.reset()}

@app.post("/step")
async def step(payload: dict = Body(...)):
    action = payload.get("action", "")
    obs, reward, done = env.step(action)
    return {"observation": obs, "reward": reward, "done": done}

def main():
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
