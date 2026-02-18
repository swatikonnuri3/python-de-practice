def greet(func):
    func()  # call the function passed as argument

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

greet(say_hello)    # prints "Hello!"
greet(say_goodbye)  # prints "Goodbye!"
##greet() is higher order function
def outer(msg):
    def inner():
        print(msg)
    return inner  # return the inner function

hi_func = outer("Hi there!")
bye_func = outer("Goodbye!")

hi_func()  # prints "Hi there!"
bye_func() # prints "Goodbye!"
#outer is higher order function as it returns a function
