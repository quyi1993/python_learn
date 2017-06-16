class Dict(dict):

     def __init__(self, **kw):
         super(Dict, self).__init__(**kw)

     def __getattr__(self, key):
         try:
             return self[key]
         except KeyError:
             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

     def __setattr__(self, key, value):
         self[key] = value

d = Dict(abc=1, b=2,c=3)
print d.get('abc'), d.get('b'), d.get('c')


d = {"a":1,"b":2,"c":3}
d2 = dict(a=11,b=22,c=33)
print d.get('a'),d.get('b'),d.get('c')
print d2.get('a'),d2.get('b'),d2.get('c')