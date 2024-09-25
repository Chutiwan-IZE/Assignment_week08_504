def countBase(seq, base): 
    return seq.count(base.upper())

def gcContent(seq): 
    return (countBase(seq, 'G') + countBase(seq, 'C'))/len(seq)

def atContent(seq): 
    return (countBase(seq, 'A') + countBase(seq, 'T'))/len(seq)

def countBasesDict(seq): 
    basesM = {}
    for base in seq:
        basesM[base] = basesM.get(base, 0)+1
    return basesM
