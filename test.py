import polars as pl
from dfcomp import dfcomp

dfa = pl.DataFrame({
    'a': [1, 2, 3],
    'b': [1, 2, 3],
    'c': [1, 2, 3],
})

dfb = pl.DataFrame({
    'a': [1, 2, 3],
    'b': [1, 2, 3],
    'c': [1, 2, 3],
})

dfc = pl.DataFrame({
    'a': [1, 2, 3],
    'b': [1, 3, 3],
    'c': [1, 2, 3],
})

dfd = pl.DataFrame({
    'b': [1, 2, 3],
    'a': [1, 2, 3],
    'c': [1, 2, 3],
})

dfe = pl.DataFrame({
    'b': [1, 2, 3],
    'a': [1, 2, 3],
    'g': [1, 2, 3],
})

dff = pl.DataFrame({
    'a': [1, 2],
    'b': [1, 2],
    'c': [1, 2],
})

dfg = pl.DataFrame({
    'a': [1, 2, 3],
    'b': ['1', '2', '3'],
    'c': [1, 2, 3],
})

print('dfa vs dfb')
print(dfcomp(dfa, dfb))
print('---------')
print('dfa vs dfc')
print(dfcomp(dfa, dfc))
print('---------')
print('dfa vs dfd')
print(dfcomp(dfa, dfd))
print('---------')
print('dfa vs dfe')
print(dfcomp(dfa, dfe))
print('---------')
print('dfa vs dff')
print(dfcomp(dfa, dff))
print('---------')
print('dfa vs dfg')
print(dfcomp(dfa, dfg))
print('---------')
