# # Define a decorator function that adds a greeting to a function's output
# def add_greeting(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return "Hello, " + result
#     return wrapper

# # Define a function that will be decorated


# @add_greeting
# def get_name():
#     return "John"


# # Call the decorated function
# print(get_name())  # Output: Hello, John

def deco(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs) + ' John'
        return r
    return wrapper


@deco
def string():
    return 'Hi'


print(string())


def string():
    return 'Hi'


print(string())
