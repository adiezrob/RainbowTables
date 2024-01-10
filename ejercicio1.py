import math, random

# La función hash
def hash(k):
    h = 2000*((int(k)*0.618)%1)
    return str(math.floor(h)).zfill(4)

# Devuelve los últimos dos digitos
def reduction(k):
    k = str(k)
    if(len(k)) <= 2:
        return k.zfill(2)
    return k[2:] 

# Función que crea una rainbow table dada la longitud de cadena y numero de cadenas
def create_rainbowtable(chain_length=4, num_chains=50):
    if num_chains > 100:
        print("num_chains debe ser menor o igual a 100")
        return 
    rt = []
    starts = sorted(random.sample(range(0,100), num_chains))
    for ind, i in enumerate(starts):
        rt.append([str(i).zfill(2)])
        for j in range(chain_length): # Aplicar las funciones de reducción y hash chain_length veces y quedarnos solo con el primer y el último valor
            if len(rt[ind]) == 1:
                rt[ind].append(hash(reduction(rt[ind][0])))
            else:
                rt[ind][1] = (hash(reduction(rt[ind][1]))) 
    # print(rt)
    return rt

# Dado un hash, una cadena y su longitud, crackear el hash (si está en la cadena)
# Si el hash no está en la cadena, devuelve None
def findInChain(passhash, first, chain_length):
    fi = first
    see = hash(first)
    if see == passhash:
        return fi
    for _ in range(chain_length):
        fi = reduction(see)
        see = hash(fi)
        if see == passhash:
            return fi
    return None

# Dado el hash que se quiere crackear, el rainbow table que se quiere utilizar,
# devuelve la password crackeada. Si no se encuentra, devuelve None
def crack(passhash, rt, chain_length):
    last = [rt[1] for i in rt]
    originalhash = passhash
    for j in range(chain_length):
        for i in range(len(rt)):
            if passhash == rt[i][1]:
                potVal = findInChain(originalhash, rt[i][0], chain_length)
                if potVal != None:
                    return potVal 
        passhash = hash(reduction(passhash))
    return None

if __name__ == "__main__":
    # rt = [['00', '0000'], ['02', '0832'], ['04', '0428'], ['11', '0539'], ['12', '0496'], ['16', '0000'], ['17', '1036'], ['18', '0651'], ['21', '1644'], ['22', '1551'], ['25', '1708'], ['27', '0832'], ['32', '0656'], ['34', '1708'], ['37', '0700'], ['38', '0656'], ['39', '1823'], ['40', '0384'], ['42', '1215'], ['43', '0700'], ['46', '0204'], ['48', '1036'], ['49', '1888'], ['51', '1215'], ['52', '0832'], ['53', '0496'], ['54', '0475'], ['58', '1328'], ['62', '0496'], ['63', '0656'], ['67', '1215'], ['69', '0607'], ['70', '1531'], ['72', '1551'], ['74', '1596'], ['76', '0428'], ['77', '0539'], ['80', '1823'], ['81', '0944'], ['84', '0651'], ['85', '0428'], ['86', '1483'], ['87', '0700'], ['88', '0607'], ['92', '1036'], ['93', '0700'], ['95', '0587'], ['96', '0204'], ['99', '1888']]
    rt = create_rainbowtable()
    cr = crack("1775",rt, 4)
    print(cr)
