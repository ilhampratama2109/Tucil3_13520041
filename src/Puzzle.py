# berisi tentang class puzzle #

class Puzzle:
    # konstruktor untuk kelas puzzle
    def __init__(self):
        self.matrik = [[(-999)for i in range(4)]
                       for i in range(4)]  # default matriks
        self.queue = []
        self.inversion = []
        self.container = {}
        self.deep = 0
        self.path = ""

    # mengubah matrik menjadi array 1 dimensi

    def convertToArray(self, matrik):
        Array = [(-999) for i in range(16)]
        indeks = 0
        for i in range(4):
            for j in range(4):
                Array[indeks] = matrik[i][j]
                indeks = indeks + 1
        return Array

    # mengubah array menjadi matrik berukuran 4x4
    def convertToMatrik(self, Array):
        matrik = [[(-999) for i in range(4)] for i in range(4)]
        indeks = 0
        for i in range(4):
            for j in range(4):
                matrik[i][j] = Array[indeks]
                indeks = indeks + 1
        return matrik

    # menghitung inversi dari matrik
    def CountInversion(self):
        count = 0
        MatrikInv = self.convertToArray(self.matrik)
        for i in range(16):
            inverseCount = 0
            for j in range(i+1, 16):
                if(MatrikInv[i] > MatrikInv[j]):
                    inverseCount = inverseCount + 1
                    count = count + 1
            self.inversion.append([MatrikInv[i], inverseCount])

        inversion = self.inversion
        inversion.sort(key=lambda inversion: inversion[0])
        return count

    # mencari baris tempat X berada (X pasti ada dalam matriks)
    def findBlankSpaceRow(self):
        for i in range(4):
            for j in range(4):
                if(self.matrik[i][j] == 16):
                    return i

    # mencari kolom tempat X berada (X pasti ada dalam matriks)
    def findBlankSpaceColumn(self):
        for i in range(4):
            for j in range(4):
                if(self.matrik[i][j] == 16):
                    return j

    # menentukan apakah koordinat tempat x berada genap atau ganjil
    # fungsi tambahan yang diperlukan untuk menentukan apakah puzzle bisa diselesaikan atau tidak
    def findBlankSpace(self):
        i = self.findBlankSpaceRow()
        j = self.findBlankSpaceColumn()
        if((i+j) % 2 == 0):
            return 0
        else:
            return 1

    # mengecek apakah puzzle bisa diselesaikan atau tidak
    def solvable(self):
        if((self.CountInversion() + self.findBlankSpace()) % 2 == 0):
            return True
        else:
            return False

    # menghitung jumlah posisi matrik yang benar
    def countPosition(self, matrik):
        count = 0
        ctr = 1
        for i in range(4):
            for j in range(4):
                if (matrik[i][j] == ctr):
                    count += 1
                ctr += 1
        return count

    # menentukan solusi jika semua matrik berada pada posisi yang seharusnya
    def isSolution(self):
        if (self.countPosition(self.matrik) != 16):
            return False
        return True

    # menampilkan matrik ke layar
    def printmatrik(self):
        for i in range(4):
            for j in range(4):
                if (self.matrik[i][j] < 10):
                    print(str(self.matrik[i][j]), end="  ")
                else:
                    if (self.matrik[i][j] == 16):
                        print("X ", end=" ")
                    else:
                        print(self.matrik[i][j], end=" ")
            print("")

    # menampilkan matrik inversi ke layar
    def printInverse(self):
        for i in range(16):
            print(str(i+1) + " : " + str(self.inversion[i][1]))
        inverse = self.CountInversion()
        print("Total : " + str(inverse))
        print("sigma KURANG(i) + X = " + str(inverse + self.findBlankSpace()))

    # mengecek apakah pergerakan valid
    def isMoveValid(self, matrik):
        # jika berada padapada baris pertama
        if (matrik[1] == 'up'):
            if (self.findBlankSpaceRow() == 1):
                return False
        # jika berada pada baris terakhir
        elif (matrik[1] == 'down'):
            if (self.findBlankSpaceRow() == 4):
                return False
        # jika berada pada kolom pertama
        elif (matrik[1] == 'left'):
            if (self.findBlankSpaceColumn() == 1):
                return False
        # jika berada pada colom terakhir
        elif (matrik[1] == 'right'):
            if (self.findBlankSpaceColumn() == 4):
                return False
        else:
            return True

    # fungsi move, digunakan untuk memindahkan blank space / X
    def move(self, matrik):
        i = self.findBlankSpaceRow() - 1
        j = self.findBlankSpaceColumn() - 1
        if (self.isMoveValid(matrik)):
            if (matrik[1] == "up"):
                matrik[0][i][j] = matrik[0][i-1][j]
                matrik[0][i-1][j] = 16
            elif (matrik[1] == "down"):
                matrik[0][i][j] = matrik[0][i+1][j]
                matrik[0][i+1][j] = 16
            elif (matrik[1] == "left"):
                matrik[0][i][j] = matrik[0][i][j-1]
                matrik[0][i][j-1] = 16
            elif (matrik[1] == "right"):
                matrik[0][i][j] = matrik[0][i][j+1]
                matrik[0][i][j+1] = 16
        return matrik

    # evaluasi path untuk menampilkan arah pergerakan
    def pathEvaluation(self):
        currPath = self.path.pop(0)
        if (currPath == 'w'):
            self.move([self.matrik, 'up'])
            print("Up")
        elif (currPath == 's'):
            self.move([self.matrik, 'down'])
            print("Down")
        elif (currPath == 'a'):
            self.move([self.matrik, 'left'])
            print("Left")
        elif (currPath == 'd'):
            self.move([self.matrik, 'right'])
            print("Right")
        else:
            pass
