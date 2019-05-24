from module2 import *

print("My name is: ", __name__, "and I'll be printed always.")

if __name__ == '__main__':
    print("Hello everyone I'm within the if __name__ == '__main__' block")


def function_one():
    print("I'm function_one from fist_module")
    # print('I am in first_module, my name is: {}'.format(__name__))

def function_two():
    print("I'm function_two from first_module")
