import os

API_BASE_URL = os.getenv("API_BASE_URL", "default")
MODEL_NAME = os.getenv("MODEL_NAME", "default")
HF_TOKEN = os.getenv("HF_TOKEN", "")

from env import EmailEnv
from agent import Agent

def run():
    print("START")

    env = EmailEnv(mode="all")
    agent = Agent()

    state = env.reset()
    done = False

    while not done:
        print("STEP")
        action = agent.act(state["email"])
        state, reward, done = env.step(action)

    print("END")

if __name__ == "__main__":
    run()