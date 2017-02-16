from doper import dope


@dope('foo')
def another(foo):
    print("This %s is from another file" % foo)