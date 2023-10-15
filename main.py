from function import *
proposition = ""
guess = []
allword = getallword()
size = sizeofword()
reduced = reducelist(allword, size)
reduce = reducedfl(reduced)

g = getgoodletters(reduce, size)

print(g)