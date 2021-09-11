import os


def txt(name, target):
    b = os.getcwd()

    if not os.path.exists(b):
        os.makedirs(b)

    txtFile = open(name + '.txt', 'a')
    if isTxt(name, target):
        txtFile.write(target)
    txtFile.close()


def isTxt(name, text):
    txtFile = open(name + '.txt', 'a+')
    result = True
    while True:
        line = txtFile.readline()
        if not line:
            break
        if text in line:
            result = False
            break

    txtFile.close()
    return result
