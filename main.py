from function import *
proposition = ""
guess = []
allword = getallword()
reduced = reducelist(allword)
reduce = reducedfl(reduced)

g = getgoodletters(reduce)

print(g)