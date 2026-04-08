import uvicorn
from fastapi import FastAPI, Body
from server.environment import SQLEnv # Ensure this matches your filename

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

# --- NEW SECTION REQUIRED BY VALIDATOR ---
def main():
    """Main entry point for the OpenEnv server."""
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860, reload=False)

if __name__ == "__main__":
    main()
