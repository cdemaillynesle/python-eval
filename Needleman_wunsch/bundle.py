import sys
from ruler import Ruler

DATASET = sys.argv[1]

with open(DATASET, "r") as dataset:
    lignes = dataset.readlines()
    # on prend les lignes 2 par 2:
    l = len(lignes) // 2
    
for i in range(l):
    A = str(lignes[2*i])
    B = str(lignes[2*i+1])
    ruler = Ruler(A, B)
    ruler.compute()
    d = ruler.distance
    top, bottom = ruler.report()
    print(f"====== example # {i} - distance = {d}")
    print(top)
    print(bottom)
    