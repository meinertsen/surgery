import types
import builtins

def wtype(object):
    return [h[:2] for h in 
               [i for j in # merge lists
                    [[[mod.__name__,k,dir(getattr(mod,k))]
                        for k in dir(mod) 
                            if isinstance(getattr(mod,k),type)] 
                        for mod in set([n for m, n in globals().items() if isinstance(n, types.ModuleType)])] 
               for i in j] # merge lists
            if set(h[2]) <= set(dir(object)) #else set(h[2]).issubset(set(dir(object))) #
          ]

    
def wis(object):
    def mergelists(ListofLists):
        return [i for j in ListofLists for i in j]
    
    return [h[:3] for h in
                mergelists(
                  [[[mod.__name__,k,getattr(mod,k)]
                          for k in dir(mod) if isinstance(getattr(mod,k),type)] 
                          for mod in set([n for m, n in globals().items() if isinstance(n, types.ModuleType)])] 
                )
            if isinstance(object,h[2])
           ]
