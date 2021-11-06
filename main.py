import _thread
from pynput.keyboard import Key, Listener
import gym

# Global var
key = None

def keypress(Key):
    global key
    key = Key

def listenKeys():
    with Listener(on_press = keypress) as listener:
        listener.join()

def game1():
    global key

    print('Starting game 1...')

    env = gym.make("CartPole-v0")
    env.reset()

    state = None

    while True:
        if key != None:
            state = None
            if str(key.char) == "a":
                state = env.step(0)
                env.render()
            elif str(key.char) == "d":
                state = env.step(1)
                env.render()
            key = None

            done = state[2]
            # Game over
            # if done:
            #    break

def game2():
    global key

    print('Starting game 2...')


    env = CartPoleEnv() #gym.make("MountainCar-v0")
    env.reset()

    state = None

    while True:
        # state = env.step(0)
        action = 1
        # action = env.action_space.sample()

        if key != None:
            state = None
            if str(key.char) == "a":
                print('key1')
                action = -1
            elif str(key.char) == "d":
                action = 1
            key = None
            state = env.step(action)

        state = env.step(action)
        print('Test')
        env.render()

        # done = state[2]
        # Game over
        # if done:
        #    break

def main():
    global key

    _thread.start_new_thread(listenKeys, ())

    game1()


if __name__ == '__main__':
    main()
