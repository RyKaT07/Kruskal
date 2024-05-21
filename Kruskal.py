class Graf:

    def __init__(self, wierzcholki, krawedzie):
        self.wierzcholki = list(set(wierzcholki))
        self.krawedzie = list(set(krawedzie))

        for krawedz in krawedzie:
            #if krawedz[0] in wierzcholki and krawedz[1] in wierzcholki
                #if krawedz[]
            for j in range(2):
                if not krawedz[j] in wierzcholki:
                    raise Exception("Nie ma mowy")

    def drzewo(self):
        wierzcholkiA = []
        wierzcholkiB = []
        sorted(self.krawedzie)
        for krawedz in range(len(self.krawedzie)):
            if (((set(self.krawedzie[krawedz][0]) & set(wierzcholkiA)) or (set(self.krawedzie[krawedz][0]) & set(wierzcholkiB))) 
                and ((set(self.krawedzie[krawedz][1]) & set(wierzcholkiA)) or (set(self.krawedzie[krawedz][1]) & set(wierzcholkiB)))):
                #raise Exception("To nie jest drzewo")
                return False
            wierzcholkiA.append(self.krawedzie[krawedz][0])
            wierzcholkiB.append(self.krawedzie[krawedz][1])
        return True

    def Kruskal(self, wagi):
        self.wagi = dict(sorted(wagi.items(), key=lambda item: item[1]))
        krawedzie_posortowane = self.wagi.keys()
        krawedzie = []
        wierzcholki = [element for krawedz in krawedzie_posortowane for element in krawedz]
        for krawedz in krawedzie_posortowane:
            krawedzie_tymczasowe = krawedzie.copy()
            krawedzie_tymczasowe.append(krawedz)
            print(krawedzie_tymczasowe)
            g = Graf(wierzcholki, krawedzie_tymczasowe)
            if(g.drzewo()==True):
                print("wykonano")
                krawedzie = krawedzie_tymczasowe.copy()
                print("wykonano")
        return krawedzie
            
        
                    
                

if __name__ == "__main__":
    g = Graf(['a','b','c','d'],[('a','b'),('b','c'),('a','d'),('b','d')])
    g.drzewo()
    print(g.Kruskal({('a','b'):1 ,('b','c'):2 , ('c','d'):5 , ('a','c'):1 , ('a','d'):1 , ('b','d'):5 , ('c','d'):2}))
    #g.Kruskal({('a','b'):1 ,('b','c'):2 , ('c','d'):5 , ('a','c'):1 , ('a','d'):1 , ('b','d'):5 , ('c','d'):2})

