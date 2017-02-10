from doper import Doper

doper = Doper(__name__)

doper.register('foo', 'bar')


@doper.dope('foo')
def injected_function(foo):
    print("injected %s" % foo)


injected_function()
