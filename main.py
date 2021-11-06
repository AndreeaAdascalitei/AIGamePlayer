import _thread
from pynput.keyboard import Key, Listener

# Global var
key = None

def keypress(Key):
    global key
    key = Key

def listenKeys():
    with Listener(on_press = keypress) as listener:
        listener.join()

def main():
    global key
    _thread.start_new_thread(listenKeys, ())

    print('Starting game...')

    import gym
    env = gym.make("CartPole-v0")
    env.reset()

    while True:
        # action = int(input("Action: "))
        if key != None:
            if str(key.char) == "a":
                env.step(0)
                env.render()
            elif str(key.char) == "d":
                env.step(1)
                env.render()
            key = None


if __name__ == '__main__':
    main()
