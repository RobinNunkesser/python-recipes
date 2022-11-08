import gym
import time
env = gym.make('CartPole-v1', render_mode="human")
env.reset()

for step_index in range(1000):
    env.render()

    # Action Space
    # ------------
    # 0 - Push cart to the left
    # 1 - Push cart to the right
    action = env.action_space.sample()
    print("{}: Action {}".format(step_index, action))

    # Observations
    # ------------
    # 0 - Cart Position
    # 1 - Cart Velocity
    # 2 - Pole Angle
    # 3 - Pole Angular Velocity
    observation, _, done, _, _ = env.step(action)
    print("Cart Position {}, Cart Velocity {}, Pole Angle {}, Pole Angular Velocity {}".format(observation[0], observation[1], observation[2], observation[3]))
    time.sleep(0.2)
    if done:
        break
env.close()
