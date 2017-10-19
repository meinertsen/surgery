import types
import builtins

def wtype(object):
    return [h[:2] for h in 
           [i for j in [[[mod.__name__,k,dir(getattr(mod,k))]
              for k in dir(mod) if isinstance(getattr(mod,k),type)] 
              for mod in set([n for m, n in globals().items() if isinstance(n, types.ModuleType)])] 
              for i in j] if dir(object) == h[2]
          ]
wtype(object)
