import uvicorn
from fastapi import FastAPI, Body, Request
from environment import SQLEnv  # Fixed import for inside the server folder

app = FastAPI()
env = SQLEnv()

@app.get("/")
def health(): 
    return {"status": "online"}

@app.post("/reset")
async def reset(request: Request):
    # This ensures the validator's POST request always works
    return {"observation": env.reset()}

@app.post("/step")
async def step(payload: dict = Body(...)):
    action = payload.get("action", "")
    obs, reward, done = env.step(action)
    return {"observation": obs, "reward": reward, "done": done}

def main():
    """Main entry point for the OpenEnv server."""
    # Note: we use "app" here because uvicorn is running from within the server package
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
