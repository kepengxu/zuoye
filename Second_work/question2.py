import numpy as np


def find_lcseque(s1, s2):
    # 生成字符串长度加1的0矩阵，m用来保存对应位置匹配的结果
    m = [[0 for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]
    # d用来记录转移方向
    d = [[None for x in range(len(s2) + 1)] for y in range(len(s1) + 1)]

    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                m[p1 + 1][p2 + 1] = m[p1][p2] + 1
                d[p1 + 1][p2 + 1] = 'k'
            elif m[p1 + 1][p2] > m[p1][p2 + 1]:
                m[p1 + 1][p2 + 1] = m[p1 + 1][p2]
                d[p1 + 1][p2 + 1] = 'l'
            else:
                m[p1 + 1][p2 + 1] = m[p1][p2 + 1]
                d[p1 + 1][p2 + 1] = 'u'
    (p1, p2) = (len(s1), len(s2))
    s = []
    while m[p1][p2]:
        c = d[p1][p2]
        if c == 'k':
            s.append(s1[p1 - 1])
            p1 -= 1
            p2 -= 1
        if c == 'l':
            p2 -= 1
        if c == 'u':
            p1 -= 1
    s.reverse()
    return ''.join(s)

if __name__=='__main__':
    s1='ASJSFSDJFKSDBSAIPOWFJSAHPADLSKADNASEODKJAKLDFNASDHDBAKDL BMAFFSDANFSABFNDHJFAFJKLSDFJSADJAEPOWFDSFSDFJKLSDFPEREWUGABDLADEIODKAJVNEHABEUPJEDLASJDDBDNFSDFLDFJKLSDFNSADKAPOEOPEAK'
    s2='QEIODJABDAAPWEIURANDGUASDBAUIELADJNFADSABAVCZCKJHADWEIOASDHJKASBAIUQPEHADBKADSIUEYABHJAPEOEIWURAHSKDJABDSJHASIUDJKDSAJKDAJDAUQJKEDABALCLKDIOAHKJABAKHUIQOAKJDAKHVZOAJKDOALEODSFADGAEGAD'
    b=find_lcseque(s1,s2)
    print(b)
