import random
import time

def sleepDummyMs(minMS, maxMS):
    time.sleep(random.uniform(minMS / 1000, maxMS / 1000))