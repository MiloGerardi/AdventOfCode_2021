defPath = "E:\documents E\python\AdventOfCode\inputs//"

def readFile(path, mode):
    f = open(path, mode)
    inputs = f.read()
    f.close()
    inputs = inputs.replace("\n", " ")
    return inputs


def splitText(string, separator):
    liste = string.split(separator)
    return liste


def strToInt(liste):
    liste2 = []
    for a in liste:
        liste2.append(a)
    return liste2
