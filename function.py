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
    return reducedfl


def getgoodletters(reducedfl, size):
    """Reduce the list of possible words based on the letters you know"""
    word = ""
    correct = ""
    while size != len(word):
        word = input("Entrez le mot :")
    while len(correct) != size:
        correct = input("Entrez les lettres correctes (0: mauvais, 1: bon) :")
    reducedex = []
    tocheck = []
    for i in range(len(word)):
        if correct[i] == "1":
            tocheck.append(word[i])
        else:
            tocheck.append("")
    print(tocheck)

    for word in reducedfl:
        for j in range(len(word)):
            if tocheck[j] != "":
                if word[j] != tocheck[j] and correct[j] == "1":
                    break
            if j == len(word) - 1:
                reducedex.append(word)

    print(len(reducedex), "mots possible")
    return reducedex
