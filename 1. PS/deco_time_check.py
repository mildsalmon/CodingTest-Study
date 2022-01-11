from datetime import datetime

def timer(func):
    def decorated():
        start = datetime.now()
        func()
        end = datetime.now()

        print(f"time is {end - start}")
    return decorated

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        start = datetime.now()
        self.func()
        end = datetime.now()

        print(f"time is {end - start}")
    