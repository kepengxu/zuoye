def bag(n, c, w, v):
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    for x in value:
        print(x)
    return value

if __name__=='__main__':
    ws='57    59     9    35    70    51     8    70    84    82    93    49    79    17    47    48     3    36    85    80    78    83    91    56    73    20     4    66    60    77    96     6    24    57    26    87    85    56    24     5    95    26    64    37    68    83    27    20    30    22'
    w=[int(i) for i in ws.split()]
    vs=' 451   147   248   453   141   234   299   295   363   484   294   146   205   147    40   380    37    51   120    196   245   179   101   224    37   100    61   218   315   241    51   382   102    63    44   214   405    76    312   289   203    80   208   412   254    23   295   185   215   301'
    v=[int(i) for i in vs.split()]
    n=len(v)
    c=1000
    result=bag(n,c,w,v)
    print(result)

