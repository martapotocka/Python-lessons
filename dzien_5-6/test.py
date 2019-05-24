class First(object):
    def __init__(self):
        print("first")

class Second(object):
    def __init__(self):
        print("second")

class Third(First, Second):
    def __init__(self):
        super().__init__()
        print("that's it")

t = Third()
