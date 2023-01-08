from nltk.inference.resolution import *
from nltk.sem import logic
read_expr = logic.Expression.fromstring

print("c - logiczna konsekwencja zbioru klazul?")
c = read_expr('lubi(Adam,Orzeszki)')
p1 = read_expr('all x.( jedzenie(x) -> lubi(Adam,x) )')
p2 = read_expr('jedzenie(Jablko)')
p3 = read_expr('jedzenie(Kurczak)')
p4 = read_expr('all x.all y.( (jada(x,y) and zyje(x)) -> jedzenie(y) )')
p5 = read_expr('jada(Bogdan,Orzeszki)')
p6 = read_expr('zyje(Bogdan)')
p7 = read_expr('all x.( jada(Bogdan,x) -> jada(Zuzia,x) )')
logic._counter._value = 0
tp = ResolutionProverCommand(c, [p1,p2,p3,p4,p5,p6,p7])
print(tp.prove())
print(tp.proof())