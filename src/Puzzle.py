# berisi tentang class puzzle #
import copy
from turtle import down


class Puzzle:
    # Konstruktor untuk kelas Puzzle #
    def __init__(self) :
        self.matrik = [[-999 for i in range(4)] for i in range(4)]
        self.inversion = []
        self.container = {}
        self.queue = []
        self.depth = 0
        self.path = ""
    
    # mengubah matrik menjadi array
    def convertToArray(self, matrik) :
        Array = [-999 for i in range(16)]
        x = 0
        for i in range(4) :
            for j in range(4) :
                Array[x] = matrik[i][j]
                x += 1
        return Array

    #mengubah array menjadi matrik
    def convertToMatrik(self, matrik) :
        matrix2D = [[-999 for i in range(4)] for i in range(4)]
        x = 0
        for i in range(4) :
            for j in range(4) :
                matrix2D[i][j] = matrik[x]
                x += 1
        return matrix2D 
    
    # menghitung jumlah inverse dari matrik
    # secara umum yang di cari adalah jumlah matrik[i] > matrik[j] dan i < j
    def countInversion(self) :
        count = 0
        matrixInv = self.convertToArray(self.matrik)
        for i in range(16) :
            inverseCount = 0
            for j in range(i+1, 16) :
                if (matrixInv[i] > matrixInv[j]) :
                    inverseCount += 1
                    count += 1
            self.inversion.append([matrixInv[i], inverseCount])
        inversion = self.inversion
        inversion.sort(key = lambda inversion: inversion[0])
        return count
    
    # menemukan indeks baris tempat 16 berada
    def indeksBlankSpaceRow(self) :
        found = False
        i = 0
        while not found :
            j = 0
            while (j < 4 and not found) :
                if (self.matrik[i][j] == 16) :
                    found = True
                j += 1
            i += 1
        return i
    
    # menemukan indeks kolom tempat 16 berada
    def indeksBlankSpaceColumn(self) :
        found = False
        i = 0
        while not found :
            j = 0
            while (j < 4 and not found) :
                if (self.matrik[i][j] == 16) :
                    found = True
                j += 1
            i += 1
        return j

    # menentukan apakah tempat 16 berada berada pada indeks ganjil atau genap
    def findBlankSpace(self) :
        i = self.indeksBlankSpaceRow()
        j = self.indeksBlankSpaceColumn()
        if ((i+j) % 2 == 0):
            return 0
        else:
            return 1

    # menentukan apakah matrik bisa diselesaikan atau tidak
    def isSolveable(self) :
        if ((self.countInversion() + self.findBlankSpace()) % 2 == 0) :
            return True
        else:
            return False

    # mengecek apakah matrik sudah sampai tujuan atau belum
    # tujuannya adalah semua posisi elemen matrik berada pada tempat yang seharusnya
    def isSolution(self) :
        if (self.countPosition(self.matrik) != 16) :
            return False
        return True
    
    # menghitung jumlah elemen matrik yang letaknya sesuai dengan tempatnya
    def countPosition(self, matrik) :
        count = 0;
        ctr = 1;
        for i in range(4) :
            for j in range(4) :
                if (matrik[i][j] == ctr) :
                    count += 1
                ctr += 1
        return count

    # menegecek apakah pergerakan valid atau tidak valid
    def isMoveValid(self, matrik) :
        if (matrik[1] == 'up') :
            if (self.indeksBlankSpaceRow() == 1) :
                return False
        elif (matrik[1] == 'down') :
            if (self.indeksBlankSpaceRow() == 4) :
                return False
        elif (matrik[1] == 'left') :
            if (self.indeksBlankSpaceColumn() == 1) :
                return False
        elif (matrik[1] == 'right') :
            if (self.indeksBlankSpaceColumn() == 4) :
                return False
        return True
         
    # prosedur untuk memindahkan blank space / 16
    def move(self, matrik) :
        i = self.indeksBlankSpaceRow() - 1
        j = self.indeksBlankSpaceColumn() - 1
        if (self.isMoveValid(matrik)) :
            if (matrik[1] == "up") :
                matrik[0][i][j] = matrik[0][i-1][j]
                matrik[0][i-1][j] = 16
            elif (matrik[1] == "down") :
                matrik[0][i][j] = matrik[0][i+1][j]
                matrik[0][i+1][j] = 16
            elif (matrik[1] == "left") :
                matrik[0][i][j] = matrik[0][i][j-1]
                matrik[0][i][j-1] = 16
            elif (matrik[1] == "right") :
                matrik[0][i][j] = matrik[0][i][j+1]
                matrik[0][i][j+1] = 16
        return matrik
    
    # prosedure untuk menampilkan arah pergerakan
    def pathEvaluation(self) :
        currPath = self.path.pop(0)
        if (currPath == 'w') :
            self.move([self.matrik, 'up'])
            print("Up")
        elif (currPath == 's') :
            self.move([self.matrik, 'down'])
            print("Down")
        elif (currPath == 'a') :
            self.move([self.matrik, 'left'])
            print("Left")
        elif (currPath == 'd') :
            self.move([self.matrik, 'right'])
            print("Right")
        else :
            pass

    # penyelesaian untuk matrik
    def solve(self) :
        posUp = 999
        posDown = 999
        posLeft = 999
        posRight = 999

        up = [copy.deepcopy(self.matrik), 'up']
        down = [copy.deepcopy(self.matrik), 'down']
        left = [copy.deepcopy(self.matrik), 'left']
        right = [copy.deepcopy(self.matrik), 'right']

        self.move(up)
        self.move(down)
        self.move(left)
        self.move(right)

        self.depth += 1
        
        if (tuple(self.convertToArray(up[0])) not in self.container) :
            posUp = 16 - self.countPosition(up[0]) + self.depth
            self.container[tuple(self.convertToArray(up[0]))] = 'up'
            self.queue.append([posUp, self.depth, self.path + 'w ', self.convertToArray(up[0])])

        if (tuple(self.convertToArray(down[0])) not in self.container) :
            posDown = 16 - self.countPosition(down[0]) + self.depth
            self.container[tuple(self.convertToArray(down[0]))] = 'down'
            self.queue.append([posDown, self.depth, self.path + 's ', self.convertToArray(down[0])])
            
        if (tuple(self.convertToArray(left[0])) not in self.container) :
            posLeft = 16 - self.countPosition(left[0]) + self.depth
            self.container[tuple(self.convertToArray(left[0]))] = 'left'
            self.queue.append([posLeft, self.depth, self.path + 'a ', self.convertToArray(left[0])])

        if (tuple(self.convertToArray(right[0])) not in self.container) :
            posRight = 16 - self.countPosition(right[0]) + self.depth
            self.container[tuple(self.convertToArray(right[0]))] = 'right'
            self.queue.append([posRight, self.depth, self.path + 'd ', self.convertToArray(right[0])])
            
        self.queue.sort()
        pop = self.queue.pop(0)
        self.matrik = self.convertToMatrik(pop[3])
        self.depth = pop[1]
        self.path = pop[2]
        
    # menampilkan matrik ke layar
    def printMatrik(self) :
        for i in range(4) :
            for j in range(4) :
                if (self.matrik[i][j] < 10) :
                    print(str(self.matrik[i][j]) + " ", end=" ")
                else :
                    if (self.matrik[i][j] == 16) :
                        print("X ", end=" ")
                    else :
                        print(self.matrik[i][j], end=" ")
            print()

    # menampilkan inversion dari matrik
    # menampilkan juga juga total sigma kurang(i) + X
    def printInverse(self) :
        for i in range(16) :
            print(str(i+1) + " : " + str(self.inversion[i][1]))
        inverse = self.countInversion()
        print("Total : " + str(inverse))
        print("sigma KURANG(i) + X = " + str(inverse + self.findBlankSpace()))