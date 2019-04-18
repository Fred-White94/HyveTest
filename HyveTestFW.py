######
import os
import sys
import numpy as np

class binarydata:
    def __init__(self,INPUT):
        print(os.path.exists(INPUT))
        self.INPUT = INPUT
        self.OUTPUT = 0
    def Compute_Output(self,n):
        with open(self.INPUT, "rb") as bf:
            data = bf.read().hex()
            print("here")
            a = bytearray.fromhex(data)
            c = np.asarray(a) 
            self.OUTPUT = bytearray(c)
            #File = open("OUTPUTTED.bin", "wb")
            #File.write(self.OUTPUT)

a = binarydata(sys.argv[1])
a.Compute_Output(1)



INPUT = np.asarray(a.OUTPUT)


def encode(INPUT):
    results = []
    for i,k in zip(INPUT[0::2], INPUT[1::2]):
        BytePair = [i,k]
        i = int(i)
        k = int(k)
        if i > len(INPUT):
            results.append('3F')
        if i == 0:
            results.append(k)
        elif i == k:
            results.extend(results[-i:])
            print('4')
        elif k > i:
            results.append('3F')
        elif i != 0 and k == 1:
            results.append(results[-i])
        else:
            results.extend(results[-i:-k+1])
    return results



results = encode(INPUT)


#def decode(INPUT):
#    AUB = []
#    decoded = []
#    for i in INPUT:
#        if i not in AUB:
#            AUB.append(i)
#            decoded.append(00)
#            decoded.append(i)
#        if i in AUB:
#            decoded.append(decoded.index(i))
    
#t = -1
#listindex = []
#while True:
#    try:
#        t = d.index(i, t + 1)
#        listindex.append(t)
#    except ValueError:
#        break


File = open(sys.argv[2], "wb")
File.write(results)




