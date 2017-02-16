from functools import wraps

_registry = {}
resolve = _registry.__getitem__
register = _registry.__setitem__
clear = _registry.clear

def resolve_dependencies(deps, kwargs):
    return {d: resolve(d) for d in deps if d not in kwargs}

def dope(*deps):
    def decorator(f):
        @wraps(f)
        def inject_deps(*args, **kwargs):
            ins = resolve_dependencies(deps, kwargs)
            return f(*args, **ins, **kwargs)
        return inject_deps
    return decorator
