from doper import Doper

dope = Doper(__name__)

dope.register('foo', 'bar')


@dope('foo')
def injected_function(foo):
    print("injected %s" % foo)


injected_function()
