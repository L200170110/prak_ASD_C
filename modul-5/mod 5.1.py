class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

    def __str__(self):
        a = self.nama + ',nim :' + str(self.nim)
        return a
    def getnim(self):
        return self.nim

c0 = MhsTif("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTif("Budi", 51, "Sragen", 230000)
c2 = MhsTif("Ahmad", 2, "Surakarta", 250000)
c3 = MhsTif("Chandra", 18, "Surakarta", 235000)
c4 = MhsTif("Eka", 4, "Boyolali", 240000)
c5 = MhsTif("Fandi", 31, "Salatiga", 250000)
c6 = MhsTif("Deni", 13, "Klaten", 245000)
c7 = MhsTif("Galuh", 5, "Wonogiri", 245000)
c8 = MhsTif("Janto", 23, "Klaten", 245000)
c9 = MhsTif("Hasan", 64, "Karanganyar", 270000)
c10 = MhsTif("Khalid", 29, "Purwodadi", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A,p,q):
        tmp  = A[p]
        A[p] = A[q]
        A[q] = tmp

def insertionSort(A):
        n = len(A)
        for i in range(1, n):
            nilai = A[i]
            pos = i
            while pos > 0 and nilai.nim < A[pos - 1].nim:
                A[pos] = A[pos - 1]
                pos = pos - 1
            A[pos] = nilai
def cetakdaftar(d):
    for i in d:
        print (i)

insertionSort(Daftar)
cetakdaftar(Daftar)
        
