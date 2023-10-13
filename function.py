allword = []
def getallword():
    """Get words from dico.txt and returns it as a list"""
    file = open("dico.txt", "r")
    for line in file.readlines():
        allword.append(line.strip())
    file.close()
    print(len(allword), "mots trouvés")
    return allword

def sizeofword():
    """Get the size of the word"""
    size = int(input("\nEntrez la taille du mot :"))
    return size

def reducelist(allword, size):
    """Based on getallword() and sizeofword(), reduces the list of possible words"""
    reduced = []
    print("\nok!")
    for word in allword:
        if len(word) == size:
            reduced.append(word)
    print(len(reduced), "mots possible")
    return reduced

def firstletter():
    """Get the first letter of the word - Could be fused with sizeofword()"""
    fl = input("Entrez la première lettre du mot :")
    return fl.upper()

def reducedfl(reduced):
    """Reduces the list of possible words based on reducelist() and firstletter()"""
    reducedfl = []
    fl = firstletter()
    print("\nOK!")
    for word in reduced:
        if word[0] == fl:
            reducedfl.append(word)
    print(len(reducedfl), "mots possible\n")
    print(reducedfl)