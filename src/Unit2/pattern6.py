n=5
i=1
while(i<=n):
    j=n
    vartoprint=97
    while(j>=i):
        print(chr(vartoprint),end=' ')
        vartoprint=vartoprint+1
        j-=1
    i=i+1
    print()