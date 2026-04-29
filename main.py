from env import EmailEnv
from agent import Agent

# Change mode here: easy / medium / hard / all of all
env = EmailEnv(mode="all")  
agent = Agent()

state = env.reset()
total_reward = 0

done = False

while not done:
    action = agent.act(state["email"])
    state, reward, done = env.step(action)
    total_reward += reward

print("Total Reward:", total_reward)
print("Accuracy:", env.correct, "/", len(env.emails))
