import uvicorn
from fastapi import FastAPI, Body, Request
# Change this line specifically:
from environment import SQLEnv 

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
    # Use the app object directly to avoid path strings
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
