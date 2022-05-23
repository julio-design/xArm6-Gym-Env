import gym, gym_xarm6
env = gym.make('xArm6Reach-v1')
print(env.action_space)
print(env.observation_space)
env.close()
