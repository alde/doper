from functools import wraps

registry = {}


class Doper:
    def __init__(self, name):
        if name in registry:
            raise RuntimeError("Doper for %s already configured" % name)
        self.name = name
        registry[self.name] = {}

    def __call__(self, *items):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                for i in items:
                    kwargs[i] = registry[self.name][i]

                return func(*args, **kwargs)
            return wrapper
        return decorator

    def register(self, key, value):
        registry[self.name][key] = value

