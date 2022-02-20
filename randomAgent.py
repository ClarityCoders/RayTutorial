import gym
from numpy import true_divide

env = gym.make('BipedalWalker-v3')
env.reset()

observation = env.reset()

while True:
    env.render()
    print(observation)
    action = env.action_space.sample()

    observation, reward, done, info = env.step(action)

    if done:
        break

env.close()