allword = []
def getallword():
    file = open("dico.txt", "r")
    for line in file.readlines():
        allword.append(line.strip())
    file.close()
    print(len(allword), "mots trouvés")
    return allword

def sizeofword():
    size = int(input("\nEntrez la taille du mot :"))
    return size

def reducelist(allword, size):
    reduced = []
    print("\nok!")
    for word in allword:
        if len(word) == size:
            reduced.append(word)
    print(len(reduced), "mots possible")
    return reduced

def firstletter():
    fl = input("Entrez la première lettre du mot :")
    return fl.upper()

def reducedfl(reduced):
    reducedfl = []
    fl = firstletter()
    print("\nOK!")
    for word in reduced:
        if word[0] == fl:
            reducedfl.append(word)
    print(len(reducedfl), "mots possible\n")
    print(reducedfl)