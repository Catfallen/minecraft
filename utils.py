from random import randint as rd

def mapTree(minx,minz,maxx,maxz):
    htreemin = 4
    htreemax = 6
    mapeamento = []
    
    xlist = []
    zlist = []
    xt = rd(minx,maxx)
    zt = rd(minz,maxz)
    pos = (xt,zt,1,rd(htreemin,htreemax))
    mapeamento.append(pos)
    xlist.append(xt)
    zlist.append(zt)
    print(f"First {pos}")
    while len(mapeamento) < 10:
        xt = rd(minx,maxx)
        zt = rd(minz,maxz)
        pos = (xt,zt,1,rd(htreemin,htreemax))
        if not pos in mapeamento:
            xlisttemp = list(filter(lambda x: abs(x-pos[0]) < 2,xlist))
            ylisttemp = list(filter(lambda y: abs(y-pos[1]) < 2,zlist))
            print(pos)
            print(f"x: {xlisttemp}")
            print(f"y: {ylisttemp}")
            
            if xlisttemp == [] and ylisttemp == []:
                mapeamento.append(pos)
                xlist.append(xt)
                zlist.append(zt)
    print(mapeamento)
    return mapeamento