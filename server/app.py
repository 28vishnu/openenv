import uvicorn
from fastapi import FastAPI, Body, Request
# FIX: Remove the dot. Uvicorn sees 'server' as the root package.
from server.environment import SQLEnv 

app = FastAPI()
env = SQLEnv()

@app.get("/")
def health(): 
    return {"status": "online"}

@app.post("/reset")
async def reset(request: Request):
    # This ensures it can handle the empty JSON {} sent by the validator
    return {"observation": env.reset()}

@app.post("/step")
async def step(payload: dict = Body(...)):
    action = payload.get("action", "")
    obs, reward, done = env.step(action)
    return {"observation": obs, "reward": reward, "done": done}

def main():
    """Main entry point for the OpenEnv server."""
    # Ensure this points to the full path so uvicorn can find it
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
