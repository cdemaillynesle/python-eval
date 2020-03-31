

class TreeBuilder:
    
    def __init__(self, text):
        self.text = text
        
    def __minimum__(dictionnaire):
        # retourne la plus petite valeur et la clé associée
        L = [(x, dictionnaire[x]) for x in dictionnaire.keys()]
        (CLE, m) = L[0]
        for tuple in L:
            if tuple[1] < m:
                CLE = tuple[0]
                m = tuple[1]
        return(CLE, m)

        
    def tree(self):
        #on analyse d'abord les occurences des lettres dans le texte
        n = len(self.text)
        dict_occ = {}
        arbre_bin = {}
        for i in range(n):
            dict_occ[self.text[i]] = 0
            arbre_bin[self.text[i]] = ""
        for i in range(n):
            dict_occ[self.text[i]] = dict_occ[self.text[i]] + 1
        #on assemble les deux plus petits poids jusqu'à ce qu'il n'y en ait qu'un    
        while len(dict_occ) > 1:
            (grp1, occ1) = minimum(dict_occ)
            for lettre in grp1:
                arbre_bin[lettre] = arbre_bin[lettre] + "0"
            dict_occ.pop(grp1)
            (grp2, occ2) = minimum(dict_occ)
            for lettre in grp2:
                arbre_bin[lettre] = arbre_bin[lettre] + "1"
            dict_occ.pop(grp2)
            dict_occ[grp1+grp2] = occ1+ occ2
        #on a maintenant associé à chaque lettre son "chemin" dans l'arbre, du bas vers le haut
        #on veut l'écrire du haut vers le bas
        for lettre in arbre_bin.keys():
            chemin_inv = arbre_bin[lettre]
            n = len(chemin_inv)
            chemin = ""
            for i in range(n):
                chemin = chemin + chemin_inv[n-i-1]
            arbre_bin[lettre] = chemin
        return(arbre_bin)
            
        
class Codec:
    
    def __init__(self, arbre):
        self.arbre = arbre
        
    def encode(self, text):
        code = ""
        for lettre in text:
            code = code + self.arbre[lettre]
        return(code)
    
    def decode(self, code):
        text = ""
        n = len(code)
        i = 0
        #on écrit l'arbre à l'envers, pour que les clés soient les codes
        arbre_inv = {}
        codes = []
        for cle in self.arbre.keys():
            arbre_inv[self.arbre[cle]] = cle
            codes.append(self.arbre[cle])
        groupe = code[i]
        while i < n-1:
            if groupe in codes:
                text = text + arbre_inv[groupe]
                i = i + 1
                groupe = code[i]
            else:
                i = i + 1
                groupe = groupe + code[i]
        #on rajoute la dernière lettre
        text = text + arbre_inv[groupe]
        return(text)
        
                


    
text = "a dead dad ceded a bad babe a beaded abaca bed"

# on analyse les fréquences d'occurrence dans text
# pour fabriquer un arbre binaire
builder = TreeBuilder(text)
binary_tree = builder.tree()


# on passe l'arbre binaire à un encodeur/décodeur
codec = Codec(binary_tree)
# qui permet d'encoder
encoded = codec.encode(text)

#print(encoded)
# et de décoder
decoded = codec.decode(encoded)

# si cette assertion est fausse il y a un gros problème avec le code
assert text == decoded
