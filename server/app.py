from fastapi import FastAPI
from pydantic import BaseModel
from env import EmailEnv
from agent import Agent

app = FastAPI()

env = EmailEnv(mode="all")
agent = Agent()

class StepInput(BaseModel):
    email: str

@app.post("/reset")
def reset():
    state = env.reset()
    return {"state": state}

@app.post("/step")
def step(input: StepInput):
    action = agent.act(input.email)
    state, reward, done = env.step(action)

    return {
        "action": action,
        "state": state,
        "reward": reward,
        "done": done
    }
