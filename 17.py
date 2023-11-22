m=float(input('quantos metros voce quer pintar?'))
m10=m*1.0
r=6
pl=18
rl=r*pl
lg=3.6
pg=25
g=r*lg
sl=(m/pl)
sg=(m/pg)
latas=(m10/rl)
galoes=((m10%rl)/g)
print('somente latas',sl)
print('preco de usar somente latas',sl)
print('somente galoes',sg)
print('preco para usar somente galoes',sl)
print('custo latas',sl,'custo galoes',sg)