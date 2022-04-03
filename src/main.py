# main program yang digunakan untuk menjalankan program

from asyncio.windows_events import NULL
from FileHandler import *
from Puzzle import *
import time
import copy


print("==== Puzzle Solver ====")
directory = input("masukkan nama file: ")
filePath = "E:/semester 4/strategi algoritma/tucil/Tucil 3/Tucil3_IF2211_Strategi_Algoritma/src/"

# membaca input file
file = Filehandler()
puzzle15 = file.bacaFile(filePath + directory)

try:
# waktu dimulai
    start = time.time()
    print("==== Puzzle =====")
    puzzle15.printMatrik()
    print("==== Kurang(i) ====")

    if(puzzle15.isSolveable()):
        puzzle15.printInverse()
        print("Puzzle bisa diselesaikan")
        print("================")
        print("= Penyelesaian =")
        temp = copy.deepcopy(puzzle15)
        puzzle15.container[tuple(puzzle15.convertToArray(puzzle15.matrik))] = 'none'
        step = 0
        while (not puzzle15.isSolution()):
            puzzle15.solve()
            step += 1

        temp.path = puzzle15.path.split(" ")
        while (len(temp.path) != 1):
            temp.pathEvaluation()
            temp.printMatrik()
            print("=================")
        print("==== Selesai ====")
        print("Jumlah simpul dibangkitkan : " + str(len(puzzle15.container) - 1))
    else:
        puzzle15.printInverse()
        print("Puzzle tidak bida diselesaikan")
        print("==============================")
    end = time.time()
    print("Time : " + str(end-start) + " detik")
except:
    print("File tidak ditemukan")