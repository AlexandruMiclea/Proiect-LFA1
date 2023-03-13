from queue import Empty


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

    def readAutomat(self, fisier):

        with open(fisier, "r") as fisierautomat:
            self.stari = [x for x in fisierautomat.readline().split()]

            #initializam matricea de tranzitii
            self.matriceTranzitii = [[list() for x in range(len(self.stari))] for i in range(len(self.stari))] 
            #print(matriceTranzitii)

            alfabet = [x for x in fisierautomat.readline().strip('\n')]
            self.aux = fisierautomat.readlines()
            for i in range(len(self.aux) - 2):
                l = [x for x in self.aux[i].strip('\n').split()]
                #print(stari.index(l[0]))
                #print(stari.index(l[2]))


                for linie in self.matriceTranzitii[self.stari.index(l[0])]:
                    for caseta in linie:
                        if l[1] in caseta:
                            NFA = True
                self.matriceTranzitii[self.stari.index(l[0])][self.stari.index(l[2])].append(l[1])
        
        
                #print(l)
            #tranzitii = [((x[0],x[1]), x[2]) for x in aux[:-2]]
            #print(tranzitii)


            self.stareInit = self.aux[-2].strip('\n')
            self.stariFinale = [x for x in self.aux[-1].split()]

        #citim cuvintele, avand grija sa citim si cuvantul nul

    def readCuvinte(self, fisier):

        with open(fisier,"r") as fisiercuv:
            aux = fisiercuv.readlines()
            for cuv in aux:
                self.cuvinte.append(cuv.strip('\n'))
        
    # verificam daca avem de-a face cu nfa sau dfa

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

    def checkWords(self):

        for word in self.cuvinte:

            lStari = list()
            lStari.append(self.stareInit)

            while lStari is not Empty:
                for litera in word:
                    for vStare in lStari:
                        newStari = list()
                        for caseta in self.matriceTranzitii[self.stari.index(vStare)]:
                            if 

        stareCurenta = self.stareInit
        
        



if __name__ == "__main__":
    x = Automat()
    x.readAutomat("automat.txt")
    x.readCuvinte("cuvinte.txt")
    x.printData()

