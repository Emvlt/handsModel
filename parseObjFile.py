import numpy as np
import matplotlib.pyplot as plt

def trim(valueInString):
    integerValue = int(abs(float(valueInString)))
    return integerValue

def parseObjFile(filePath='test_1.obj'):
    obj_file = open(filePath)
    mat = np.zeros((300,300,300), np.uint8)

    for line in obj_file:
        if line[0] == "#" or line[0] == "m" or line[0]=='o':
            pass
            
        elif line[0]=='v':
            index1 = line.find(" ") + 1
            index2 = line.find(" ", index1 + 1)
            index3 = line.find(" ", index2 + 1)

            mat[trim(line[index1:index2]), trim(line[index2:index3]), trim(line[index3:-1])] += 1

        else:
            return mat

fileName = 'test_1'
objFileName = fileName+'obj'
npyFileName = fileName+'npy'
mat = parseObjFile(objFileName)
np.save(npyFileName, mat)