class Manusia(object):
    keadaan="lapar"
    def __init__(self,nama):
        self.nama=nama
    def ucapkanSalam(self):
        print("Salam, namaku", self.nama)
    def makan(self,s):
        print("Saya baru saja makan", s)
        self.keadaan="kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan="lapar"
    def mengalikanDenganDua(self,n):
        return n*2
    
class SiswaSMA(Manusia):
    """Class SiswaSMA yang dibangun dari class Manusia"""
    def __init__(self,nama,no_induk,kelas,alamat):
        """Metode inisialisasi ini menutupi metode inisiasi di class Manusia."""
        self.nama = nama
        self.no = no_absen
        self.kelas = kelas
        self.alamat = alamat
    def __str__(self):
        a = "Nama : "+self.nama+'\n'+"No Absen : "+str(self.no)+'\n'+"Asal dari : "+self.alamat+'\n'+"Kelas : "+str(self.kelas)
        print (a)
    def ambilNama(self):
        print (self.nama)
    def ambilNoInduk(self):
        print (self.no)
    def ambilKelas(self):
        print (self.kelas)
    def ambilAlamat(self):
        print (self.alamat)
