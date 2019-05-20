#nomor 1
class stack():
    def __init__ (self) :
        self.list = []
    def Empty (self) :
        return len(self.list) == 0
    def __len__ (self) :
        return len(self.list)
    def pop(self) :
        assert not self.Empty()
        return self.list.pop()
    def push(self, data) :
        self.list.append(data)

def cetakHexa(d) :
    f = stack()
    if d==0: f.push(0);
    while d !=0:
        sisa = d%16
        d = d//16
        f.push(sisa)
    hexa = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    st = ''
    for i in range(len(f)):
        st += str(hexa[f.pop()])
    return st

#nomor 2
class stack():
    def __init__ (self) :   #membuat stack kosong
        self.list = []
    def Empty (self) :      #mengembalikan nilai boolean yang menunjukkan apakah stack itu kosong
        return len(self.list) == 0
    def __len__ (self) :    #mengembalikan banyaknya item di stack
        return len(self.list)
    def pop(self) :         #mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.Empty()
        return self.list.pop()
    def push(self, data) :  #mendorong item ke stack, menambah item ke puncak stack
        self.list.append(data)

nilai = stack()
for i in range(16) :
    if i % 3 == 0 :
        nilai.push(i)
st = ''
for i in range(len(nilai)):
        st = st +""+ str(nilai.pop())
        print (st)
print ('***************************************************************')
    
#nomor 3
class stack():
    def __init__ (self) :    #membuat stack kosong
        self.list = []
    def Empty (self) :       #mengembalikan nilai boolean yang menunjukkan apakah stack itu kosong
        return len(self.list) == 0
    def __len__ (self) :     #mengembalikan banyaknya item di stack
        return len(self.list)
    def pop(self) :          #mengembalikan nilai posisi atas lalu menghapus, stack kosong tidak dapat kosong
        assert not self.Empty()
        return self.list.pop()
    def push(self, data) :   #mendorong item ke stack, menambah item ke puncak stack
        self.list.append(data)

nilai = stack ()
for i in range(16):
    if i % 3 == 0:
        nilai.push(i)
    elif i % 4 == 0:
        nilai.pop()
st = ''
for i in range(len(nilai)):
        st = st+""+ str(nilai.pop())
        print (st)
