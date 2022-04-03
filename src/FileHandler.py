# program ini digunakan untuk membaca inputan dari file dan menyimpannya kedalam bentuk matrik #

from Puzzle import Puzzle


class Filehandler:
    # konstruktor dari kelas FileHandler #
    def __init__(self):
        pass

    # membaca file dan mengubahnya kedalam bentuk matrik #
    def bacaFile(self, namafile):
        file = open(namafile, "r")
        temp = file.readline()
        matrik = []  # inisialisasi matrik
        for element in temp:
            elmt = element.strip("\n").split(" ")
            matrik.append(elmt)

        for i in range(4):
            for j in range(4):
                # matrik yang kosong, dimisalkan dengan X, lalu akan diubah menjadi 16 agar mempermudah perhitungan #
                if(matrik[i][j] == 'X'):
                    matrik[i][j] = 16
                else:  # mengganti tipe element matrik ke dalam bentuk integer #
                    matrik[i][j] = int(matrik[i][j])
        puzzle = Puzzle()
        puzzle.matrik = matrik
        return puzzle
