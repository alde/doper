from doper import dope, register


register('foo', 'bar')

@dope('foo')
def injected_function(foo):
    print("injected %s" % foo)

injected_function()


import example2
example2.another()