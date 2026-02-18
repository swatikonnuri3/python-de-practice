def my_deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@my_deco
def say_hello():
    print("hello swati")
say_hello()