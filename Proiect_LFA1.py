import copy

class Automat:

#citim automatul

    def __init__(self):

        self.stari = list()
        self.alfabet = list()
        self.matriceTranzitii = list()
        self.stareInit = ""
        self.stariFinale = list()
        self.cuvinte = list()
        self.NFA = False
        self.solutii = list()

        self.drumCurent = list()

    def readAutomat(self, fisier):

        with open(fisier, "r") as fisierautomat:
            self.stari = [x for x in fisierautomat.readline().split()]

            #initializam matricea de tranzitii
            self.matriceTranzitii = [[list() for x in range(len(self.stari))] for i in range(len(self.stari))] 
            #print(matriceTranzitii)

            self.alfabet = [x for x in fisierautomat.readline().strip('\n')]
            self.aux = fisierautomat.readlines()
            for i in range(len(self.aux) - 2):
                l = [x for x in self.aux[i].strip('\n').split()]

                #verificam daca am facut o greseala de redactare
                if l[0] not in self.stari:
                    raise ValueError(f"Starea {l[0]} nu este definita!")
                if l[2] not in self.stari:
                    raise ValueError(f"Starea {l[2]} nu este definita!")
                if l[1] not in self.alfabet:
                    raise ValueError(f"Litera {l[1]} nu este definita!")

                #print(stari.index(l[0]))
                #print(stari.index(l[2]))

                # verificam daca avem de-a face cu nfa sau dfa
                for linie in self.matriceTranzitii[self.stari.index(l[0])]:
                    for caseta in linie:
                        if l[1] in caseta:
                            self.NFA = True

                self.matriceTranzitii[self.stari.index(l[0])][self.stari.index(l[2])].append(l[1])

            self.stareInit = self.aux[-2].strip('\n')
            self.stariFinale = [x for x in self.aux[-1].split()]

    #citim cuvintele, avand grija sa citim si cuvantul nul
    def readCuvinte(self, fisier):

        with open(fisier,"r") as fisiercuv:
            aux = fisiercuv.read().split('\n')
            for cuv in aux:
                self.cuvinte.append(cuv.strip('\n'))

                litereCuv = set([x for x in cuv.strip('\n')])
                #print(litereCuv)
                for el in litereCuv:
                    if el not in self.alfabet:
                        raise ValueError(f"Litera {el} nu este definita!")
        
    #afisam datele dupa citire
    def printData(self):

        print(self.stari)
        print(self.alfabet)
        print(self.stareInit)
        print(self.stariFinale)
        print(self.cuvinte)
        print(self.NFA)

        for i in self.matriceTranzitii:
            for j in i:
                print(j, end=' ')
            print()


    def DFS(self, nod, cuvant):

        self.drumCurent.append(nod)
        cDrumCurent = copy.deepcopy(self.drumCurent)
        stariNoi = list()

        if cuvant:

            litera = cuvant[0]
            cuvant = cuvant[1:]

            for i in range(len(self.matriceTranzitii[self.stari.index(nod)])):
                if litera in self.matriceTranzitii[self.stari.index(nod)][i]:
                    stariNoi.append(self.stari[i])

            for el in stariNoi:
                self.DFS(el, cuvant)
                self.drumCurent = cDrumCurent

        else:
            if nod in self.stariFinale:
                self.solutii.append(self.drumCurent)

        #adauga nodul curent in lista
        #vezi unde te poti duce cu prima litera pe graf
            #daca nu mai sunt litere vezi daca esti stare finala
                #daca da, da append listei la raspunsuri
            #daca mai sunt litere
            #dfs pe lista de litere
        #


        return

    def checkWords(self, fisier = ""):

        tipAutomat = "AFN" if self.NFA else "AFD"
        print(f"Aici avem un {tipAutomat}.")

        for word in self.cuvinte:

            self.solutii = list()
            self.drumCurent = list()

            self.DFS(self.stareInit, word)

            if self.solutii:
                if fisier != "":
                    with open(fisier, "a") as output:
                        output.write(f"Automatul acesta este finit pentru cuvantul {word}!\n")
                        output.write("Drumurile cu care ajungem in stare finita sunt:\n")
                        for lista in self.solutii:
                            for el in lista:
                                output.write(str(el) + " ")
                        output.write('\n')
                print(f"Automatul acesta este finit pentru cuvantul {word}!")
                print("Drumurile cu care ajungem in stare finita sunt:")
                for lista in self.solutii:
                    print(*lista)
            else:
                word = "vid" if word == "" else word
                if fisier != "":
                    with open(fisier, "a") as output:
                        output.write(f"Automatul acesta NU este finit pentru cuvantul {word}!")
                word = u'\u03bB' if word == "vid" else word
                print(f"Automatul acesta NU este finit pentru cuvantul {word}!")




if __name__ == "__main__":
    x = Automat()
    x.readAutomat("automat.txt")
    x.readCuvinte("cuvinte.txt")
    #x.printData()
    x.checkWords("output.out")

