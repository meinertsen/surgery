import types
import builtins

def wtype(object):
    test=dir(object)
    return [b[1] for b in 
           [i for j in [[[k.__name__,i,dir(getattr(k,i))]
              for i in dir(k) if isinstance(getattr(k,i),type)] 
              for k in (types,builtins)] 
              for i in j] if test == b[2]
          ]
