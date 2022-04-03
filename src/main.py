# main program yang digunakan untuk menjalankan program

from FileHandler import *
from Puzzle import *
import time
import copy


print("==== Puzzle Solver ====")
dir = input("masukkan nama file: ")
# try:
# membaca input file
file = Filehandler()
puzzle15 = file.bacaFile(dir)

# waktu dimulai
start = time.time
print("==== Puzzle =====")
print("==== Kurang(i) ====")

if(puzzle15.solvable()):
    puzzle15.printInverse()
    print("Puzzle bisa diselesaikan")
    print("================")
    print("= Penyelesaiam =")
    temp = copy.deepcopy(puzzle15)
    puzzle15.container[tuple(
        puzzle15.convertToArray(puzzle15.matrik))] = 'none'
    step = 0
    while (not puzzle15.isSolution()):
        puzzle15.solve()
        step += 1

    temp.path = puzzle15.path.split(" ")
    while (len(temp.path) != 1):
        temp.pathEvaluation()
        temp.printmatrik()
        print("=================")
    print("==== Selesai ====")
    print("Jumlah simpul dibangkitkan : " +
          str(len(puzzle15.container) - 1))

# except:
#     print("File tidak ditemukan")
