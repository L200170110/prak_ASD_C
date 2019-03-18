class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        self.checkSizeConsis()
        self.checkTypeConsis()

    def checkSizeConsis(self):
        for allcol in self.matrix:
            if len(allcol) != self.col:
                raise ValueError("Jumlah kolom tidak sama/konsisten")

    def checkTypeConsis(self):
        typedata = type(self.matrix[0][0])
        for x in self.matrix:
            for y in x:
                if type(y) != typedata:
                    raise ValueError("Tipe data di dalam matrix tidak sama/konsisten")

    def getSize(self):
        return (self.row, self.col)

    def transposeX(self):
        m = len(self.matrix)
        n = len(self.matrix[1])
        d = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                d[j][i] = self.matrix[i][j]
        return d

    def addMatrix(self, objMatrix):
        if objMatrix.row != self.row and objMatrix.col != self.col:
            return "Ukuran matrix tidak konsisten"
        final = []
        for [x,y] in zip(self.matrix, objMatrix.matrix):
            colTemp = []
            for a,b in zip(x, y):
                colTemp.append(a+b)
                if len(colTemp) == self.col:
                    final.append(colTemp)
                    colTemp = []
        return final

    def multiplyMatrix(self, objMatrix):
        if self.row != objMatrix.col and self.col != objMatrix.row:
            return "Syarat perkalian matrix tidak memenuhi"
        newObjMatrix = objMatrix.transposeX()
        final = []
        for x,y in zip(self.matrix, newObjMatrix):
            colTemp = []
            for a,b in zip(x, y):
                colTemp.append(a*b)
                if len(colTemp) == self.col:
                    final.append(colTemp)
                    colTemp = []
        return final
    def determinan2x2(self):
        if self.row != 2 and self.col != 2:
            return "Hanya matrix 2x2"
        det = (self.matrix[0][0]*self.matrix[1][1])-(self.matrix[0][1]*self.matrix[1][0])
        return det



a = Matrix([[1,2,3,4],[5,6,7,8],[5,6,7,8]])
b = Matrix([[11,12,13,14],[15,16,17,18],[5,6,7,8]])
print(a.getSize())
print(a.addMatrix(b))

c = Matrix([[1, 2, 3], [4, 5, 6]])
d = Matrix([[1, 2], [3, 4], [5, 6]])
print(c.multiplyMatrix(d))
c.multiplyMatrix(d)

e = Matrix([[1, 2], [3, 4]])
print(e.determinan2x2())

