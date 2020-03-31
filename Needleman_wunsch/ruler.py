import numpy as np
from colorama import Fore, Style

def red_text(text):
    return(f"{Fore.RED}{text}{Style.RESET_ALL}")
    
class Ruler:
    
    def __init__(self, A, B):
      self.A = A
      self.B = B
      
    def compute(self):
        #coût de substitution
        substi = 1
        #coût d'insertion
        self.d = 1
        n = len(self.A)
        m = len(self.B)
        F = np.zeros((n, m))
        #F(i,j) est la distance optimale pour l'alignement des i premiers caractères de B et les j premiers caractères de A
        for i in range(n):
            F[i,0] = self.d*i
        for j in range(m):
            F[0,j] = self.d*j
            
        for i in range(1, n):
            for j in range(1, m):
                if self.A[i] == self.B[j]:
                    s = 0
                else:
                    s = substi
                F[i,j] = min(F[i-1,j-1]+s, F[i, j-1]+self.d, F[i-1,j]+self.d)
                
        #F(n,m) est donc la distance optimale pour l'alignement de tous les caractères de A et B
        
        self.distance = F[n-1, m-1]
        self.F = F
        

    def report(self):
        #on retrace le chemin suivi dans la matrice F pour déterminer quand il y a eu substitution / ajout / délétion
        F = self.F
        nouv_A = ""
        nouv_B = ""
        (i,j) = F.shape
        i = i - 1
        j = j - 1
        while i > 0 and j > 0:
            F_diag = F[i-1,j-1]
            F_haut = F[i-1,j]
            F_gauche = F[i, j-1]
            if F[i,j] == F_haut + self.d :
                #le ième caractère de A est aligné à un trou
                nouv_B = red_text("=") + nouv_B
                i = i -1
            elif F[i,j] == F_gauche + self.d :
                #le jème caractère de B est aligné avec un trou
                nouv_A = red_text("=") + nouv_A
                j = j-1
            else:
                if F[i,j] == F_diag :
                    #ième caractère de A = jème caractère de B
                    nouv_A = self.A[i] + nouv_A
                    nouv_B = self.B[j] + nouv_B
                    
                else:
                    #il y a substitution
                    nouv_A = red_text(self.A[i]) + nouv_A
                    nouv_B = red_text(self.B[j]) + nouv_B
                i = i - 1
                j = j - 1
        if self.A[i] != self.B[j] :
            nouv_A = red_text(self.A[i]) + nouv_A
            nouv_B = red_text(self.B[j]) + nouv_B
        else:
            nouv_A = self.A[i] + nouv_A
            nouv_B = self.B[j] + nouv_B
        if i == 0:
            nouv_A = red_text(j*"=") + nouv_A
        elif j == 0:
            nouv_B = red_text(i*"=") + nouv_B
            
        return(nouv_A, nouv_B)
        


        

                