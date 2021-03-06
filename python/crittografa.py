consonantiMax = [
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'B']
consonantiMin = [i.lower() for i in consonantiMax]  # consonanti minuscole
vocaliMax = ['A', 'E', 'I', 'O', 'U', 'Y', 'A']
vocaliMin = [i.lower() for i in vocaliMax]
numeriList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

nuovaParola = []

def converti(lettera):
    if lettera in consonantiMax:
        nuovaParola.append(consonantiMax[consonantiMax.index(lettera)+1])
    elif lettera in consonantiMin:
        nuovaParola.append(consonantiMin[consonantiMin.index(lettera)+1])
    elif lettera in vocaliMax:
        nuovaParola.append(vocaliMax[vocaliMax.index(lettera) + 1])
    elif lettera in vocaliMin:
        nuovaParola.append(vocaliMin[vocaliMin.index(lettera) + 1])
    elif lettera in numeriList:
        nuovaParola.append(numeriList[numeriList.index(lettera) + 1])
    else:
        nuovaParola.append(lettera)

parole = ''

with open('input.txt', 'r') as fin:
    for line in fin.readlines():
        parole += line

for i in parole:
    converti(i)


with open('output.txt', 'w') as fout:
    for i in nuovaParola:
        fout.write(i)

