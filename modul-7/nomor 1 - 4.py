# nomor 1

import re
f = open("Indonesia.txt", "r")
pola = r"me[\w\.-]+"
tampil = re.findall(pola, f.read())
print(tampil)

print ("***********************************************************")

#nomor 2
import re
f = open("Indonesia.txt", "r")
pola2 = r"di[\w\.-]+"
tampil2 = re.findall(pola2, f.read())
print(tampil2)

print ("***********************************************************")

#nomor 3
import re
f = open("Indonesia.txt", "r")
pola3 = r"di\s[\w\.-]+"
tampil3 = re.findall(pola3, f.read())
print(tampil3)

print ("***********************************************************")

#nomor 4a

import re
f = open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
p4=r'([\w+]+)</a></td>'
string=re.findall(p4,teks4)
print(string)

#Nomor 4b

f = open('KEI.html','r', encoding='latin1')
teks4 = f.read()
f.close()
string=re.findall(r'title="([\w+]+)">',teks4)
string=re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks4)
a=[]
for i in string:
    a.append((i[0], float(i[1])))
print(a)
