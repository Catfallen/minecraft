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


def leafs(c,h):
    maxx = c[0]+3
    minx = c[0]-3
    maxz = c[1]+3
    minz = c[1]-3
    
    middle = list(range(minx,maxx+1))
    print(middle)
    
    inicial = 0
    for y in range(inicial,h):
        folhas = 0
        if y % 2 == 0 and y != inicial+2 and y >=2:    
            maxx-=1
            minx+=1
            maxz-=1
            minz+=1
        
        if y >= 2:
            for x in range(minx,maxx+1):
                for z in range(minz,maxz+1):
                #print(x,y,z,end = " ")
                    if x == c[0] and z == c[1]:
                        print("wood")
                    else:
                        folhas += 1
                    #print(f"leaf: {folhas}")
        print(f"Folhas de {y}: {folhas}")
            
    pass