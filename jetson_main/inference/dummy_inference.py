from time import sleep
import random

CATEGORIES = ['bandage', 'tape', 'cold compress']

def dummy_inference():
    sleep(0.05)
    return random.choice(CATEGORIES)