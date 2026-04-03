from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailEnv
from agent import Agent

app = FastAPI()

class StepInput(BaseModel):
    email: str

@app.post("/reset")
def reset():
    env = EmailEnv(mode="all")
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(input: StepInput):
    env = EmailEnv(mode="all")
    agent = Agent()

    action = agent.act(input.email)
    state, reward, done = env.step(action)

    return {
        "action": action,
        "state": state,
        "reward": reward,
        "done": done
    }


def main():
    return app


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)
