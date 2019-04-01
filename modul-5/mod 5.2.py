def insertionSort(A):
        n = len(A)
        for i in range(1, n):
            nilai = A[i]
            pos = i
            while pos > 0 and nilai < A[pos - 1]:
                A[pos] = A[pos - 1]
                pos = pos - 1
            A[pos] = nilai
A = [1,3,5,7,9,11,13,15,17,19,21,23]
B = [2,4,6,8,10,12,14,16,18,20,22,24]
C = []

C.extend(A)
C.extend(B)
insertionSort(C)
print ('Nilai C :', C) 
