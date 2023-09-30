
import numpy as np

class matrixObj(object):
   
    def __init__(self, matrix):
            self.__matrix = matrix

    @property
    def matrix(self):
        return self.__matrix
        
    @matrix.setter
    def matrix(self, matrix):
        matrixObjCnt = len(matrix[:][0])
        for obj in range(0, len(matrix[:])-1):
             if(len(matrix[obj]) != matrixObjCnt):
                  raise ValueError("Matrix is not proper")
        #self.__matrix = self.matrix
             
    def __checkMatrixCompatibility(self, other):
        for col in range(0, len(self.__matrix[:])):
            if(len(self.__matrix[col]) != len(other.__matrix[:])):
                raise ValueError("Matricises are not compatible")
            
    def __mul__(self, other):
        #print(self.__matrix[0][:])
        colSum = 0
        resMatrix = []
        self.__checkMatrixCompatibility(other)

        for mat1row in self.__matrix[:]:
            resRow = []
            print(len(other.matrix[:]))
            for mat2Col in range(0, len(other.__matrix[0][:])):
                for ind, mat1col in enumerate(mat1row):        
                    colSum += mat1col*other.__matrix[ind][mat2Col]
                    print(mat1col, other.__matrix[ind][mat2Col])
                resRow.append(colSum)
                print(resRow)

                if(len(resRow[:]) == len(other.__matrix[0][:])):
                    resMatrix.append(resRow)
                colSum = 0
        return resMatrix
         
             #4x3
mar = matrixObj([
                [1,2,3],
                [2,3,4], 
                [6,8,9],
                [10,11,12], 

                 ])
            #3x2
mar2 = matrixObj([[1,2],
                  [2,2],
                  [3,4]])

mar*mar2
