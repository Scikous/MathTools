
import numpy as np

class VectorObj(object):
   
    def __init__(self, vect):
            self.vect = vect
    
    def tupleCheck(self, other):
        if not isinstance(self.vect, tuple) or not isinstance(other.vect, tuple): #check if vectors are tuples
            raise ValueError("Vect must be tuple")
        else:
            if not len(self.vect) == len(other.vect):
                raise ValueError("Vectors must have the same amount of values in them")
            else:
                return 0
 
    #adds together vectors when using the addition operator
    def __add__(self, other):
        self.tupleCheck(other)
        resVect = []

        for v1, v2 in zip(self.vect, other.vect):
            resVect.append(v1+v2)
        resVect = tuple(resVect)
        return VectorObj(resVect)
    
    #subtracts two vectors when using the addition operator 
    def __sub__(self, other):
        self.tupleCheck(other)

        resVect = []
        for v1, v2 in zip(self.vect, other.vect):
            resVect.append(v1-v2)
        resVect = tuple(resVect)
        return VectorObj(resVect)
    
    #dot product vectors
    def __mul__(self, other):
        self.tupleCheck(other)
        result = 0

        for v1, v2 in zip(self.vect, other.vect):
            result += v1+v2
        return VectorObj(result)
    
    #multiply vector by some value
    def __rmul__(self, other):
        multiplier = other
        if(isinstance(multiplier, int)):
            resVect = []
            for v1 in self.vect:
                resVect.append(v1*multiplier)
            resVect = tuple(resVect)
            return VectorObj(resVect)
        else:
            raise ValueError("given multiplier is not an int")

    
    def __str__(self):
        return str(self.vect)


u = (2, -1, 0, -3)
w = (1,3,-2,2)
v = (1,-1,-1,3)

# print(np.add(u,v,w))

# u3 = tuple(3*val for val in u)
# UplusV = tuple(uVal+vVal for uVal, vVal in zip(u, v))
# U2minusV3 = tuple(2*uVal-3*vVal for uVal, vVal in zip(u, v))
# U5minusV3minusW4 = tuple(5*uVal-3*vVal-4*wVal for uVal, vVal, wVal in zip (u, v, w))
# negUplusV2minusW2 = tuple(-1*uVal+2*vVal-2*wVal for uVal, vVal, wVal in zip (u, v, w))



#print(3*np.array(u))


obj = VectorObj(u)
ob2 =VectorObj(v)
ob3 =VectorObj(w)


res = obj+ob2-ob3
res2 = obj*ob3

print(res, res2, 3*obj)