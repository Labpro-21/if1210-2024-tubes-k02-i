# KAMUS
# seed : integer
# ALGORITMA
from time import time
seed = int(time())
# seed akan terus berubah
# Mengembalikan angka random dengan algoritma Linear Congruential Generator (LCG) dengan angka rentang 0 - batas_atas.
#seed: Nilai awal (biji) untuk memulai urutan.
#a: Pengganda dalam rumus LCG.
#c: Penambahan dalam rumus LCG.
#m: Modulus dalam rumus LCG.

#rumus LCG= (a*seed + b) mod m
#syarat : 0<m , 0<a<m , 0<=x<m, 0<seed<m
def LCG(batas_atas : int) -> int:
    # KAMUS LOKAL:
        #const a : integer = 1664525
        # constb c : integer = 1013904223
        # const m : integer = 2^32
    
    # ALGORITMA
    a = 1664525
    c = 1013904223
    m = 2**32
    global seed
    seed = (a*seed + c) % m
    return seed % (batas_atas + 1)
