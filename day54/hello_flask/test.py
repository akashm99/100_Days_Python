def decorator_function(function):
    def wrapper():
        function()
    return wrapper

