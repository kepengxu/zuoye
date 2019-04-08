#coding:utf-8
def matrix_print(s,i,j):
    if i==j:
        print("A[%d]"%(i),end='')
    else:
        print("(",end='')
        matrix_print(s,i,s[i][j])
        matrix_print(s,s[i][j]+1,j)
        print(")",end='')

def matrix_memoed(p):
    n = len(p) - 1
    memozed_list = []
    s = []
    for i in range(n + 1):
        memozed_list.append([-1 for i in range(n + 1)])
        s.append([0 for i in range(n + 1)])
    matrix_help(memozed_list, p, s, 1, n)
    for i in memozed_list[1:]:
        pass
 #       print(i)
    matrix_print(s, 1, n)


def matrix_help(memozed_list, p, s, i, j):
    if (memozed_list[i][j] >= 0):
        return memozed_list[i][j]
    if (i == j):
        memozed_list[i][j] = 0
        return memozed_list[i][j]
    memozed_list[i][j] = 99999999
    for k in range(i, j):
        q = matrix_help(memozed_list, p, s, i, k) + matrix_help(memozed_list, p, s, k + 1, j) + p[i - 1] * p[k] * p[j]
        if (q < memozed_list[i][j]):
            memozed_list[i][j] = q
            s[i][j] = k
    return memozed_list[i][j]

if __name__=='__main__':
    s='85    61    65    94    35    36    50    97    57   100    70    75    85    70    90    31    70    81    27    90    19    37    35    74    81    95    12    61    97     4     5     6    94    13     6    21    49    59    71    44    89    14    64    35    55    84    63    61    27    89    53'
    l=[int(i) for i in s.split()]
    print(l)
    matrix_memoed(l)


