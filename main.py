import copy

def Inchideri(dict, dictinchideri):
    lmb='l'
    closure={}
    if lmb in dict:
        L=dict[lmb]
    #aflam inchiderea fiecarei stari
    print(L)
    for t in L:
        dictinchideri[t[0]].add(t[1])
    ok=1
    while ok==1:
        ok=0
        dictinchideri_copy = {}
        for k, v in dictinchideri.items():
            temp_set = set(v)
            dictinchideri_copy[k] = set(temp_set)
        for cheie in dictinchideri_copy :
            lista = []
            for el in dictinchideri_copy [cheie]:
                for t in L:
                    if el==t[0]:
                        lista.append(t[1])
            for el in lista:
                dictinchideri[cheie].add(el)
        if dictinchideri!=dictinchideri_copy:
            ok=1
    return dictinchideri


def transformareDFA(tranzitiiNFA, inchideriNFA): #transformam lambda NFA in DFA
    dictDFA={}
    for cheie in inchideriNFA:
        if inchideriNFA[cheie] not in list(dictDFA):
            if len(inchideriNFA[cheie])==1 and len(inchideriNFA[cheie])>0:
                ok=0
                for elemente in dictDFA:
                    for element in elemente:
                        if element==inchideriNFA[cheie]:
                            ok=1
                if ok==0:
                    ok=1
                    for x in dictDFA:
                        if isinstance(x, tuple):
                            for el in x:
                                stare=''.join(inchideriNFA[cheie])
                                if stare==el:
                                    ok=0
                    if ok==1:
                        dictDFA[''.join(inchideriNFA[cheie])]= {}
            elif len(inchideriNFA[cheie])>1:
                print(inchideriNFA[cheie])
                dictDFA[tuple(inchideriNFA[cheie])]= {}


    for tuplu in dictDFA:
        dictDFA[tuplu]={}
        for litera in tranzitiiNFA:
            if litera!='l':
                l = {litera: []}
                for t in tranzitiiNFA[litera]:
                    if isinstance(tuplu, tuple):
                        for x in tuplu:
                            if t[0] ==x:
                                for el in inchideriNFA[t[1]]:
                                    if el not in l[litera]:
                                        l[litera].append(el)
                    else:
                        if t[0]==tuplu:
                            for el in inchideriNFA[t[1]]:
                                if el not in l[litera]:
                                    l[litera].append(el)

                dictDFA[tuplu].update(l)  #adaugam tranzitiile respective tuplului pt fiecare litera(la fiecare stare aflata in reuniune adaugam inchiderea sa)
    print(dictDFA)

    while True:
        dictDFA_copy={}
        dictDFA_copy = copy.deepcopy(dictDFA)
        print(dictDFA_copy)
        # adaugam starile care nu se afla deja in dictionar si tranzitiile corespunzatoare
        for tuplu in dictDFA_copy:
            for litera in dictDFA_copy[tuplu]:
                if len(dictDFA_copy[tuplu][litera])>1:
                    if tuple(dictDFA_copy[tuplu][litera]) not in dictDFA:
                        dictDFA[tuple(dictDFA_copy[tuplu][litera])]={}
                        for lit in tranzitiiNFA:
                            if lit != 'l':
                                l = {lit: []}
                                print(tuple(dictDFA_copy[tuplu][litera]),lit)
                                for t in tranzitiiNFA[lit]:
                                    for x in tuple(dictDFA_copy[tuplu][litera]):
                                        if x==t[0]:
                                            for el in inchideriNFA[t[1]]:
                                                l[lit].append(el)
                                if tuple(dictDFA_copy[tuplu][litera]) in dictDFA:
                                    dictDFA[tuple(dictDFA_copy[tuplu][litera])].update(l) # adaugam tranzitiile respective tuplului pt fiecare litera(la fiecare stare aflata in reuniune adaugam inchiderea sa)

        #eliminam starile singure care se afla in alt tuplu
        dictDFA_copy2 = copy.deepcopy(dictDFA)
        for stare in dictDFA_copy2:
            if isinstance(stare,tuple)==False:
                for stare2 in dictDFA_copy2:
                    if isinstance(stare2,tuple)==True:
                        if stare in stare2:
                            del dictDFA[stare]

        if dictDFA==dictDFA_copy:
            return dictDFA


f = open("inputLambdaNFA.in", "r")
g = open("outputDAF.out", "w")
tranzitii = {}
n = int(f.readline())
stare_actuala = f.readline().strip()
inchideri={}
for _ in range(n):       #cream dictionarul ce are drept chei literele, cu l am notat lambda, si adugam fiecarei chei tranzitiile specifice
    qi, l, qf = f.readline().split()
    if l not in tranzitii:
        tranzitii[l]=[(qi, qf)]
        inchideri[qi]={qi}
        inchideri[qf] = {qf}
    else:
        tranzitii[l].append((qi,qf))
        inchideri[qi]={qi}
        inchideri[qf] = {qf}

print(tranzitii)

inchideri=Inchideri(tranzitii,inchideri)
for cheie in inchideri:
    inchideri[cheie]=sorted(inchideri[cheie])
print(inchideri)

dfa=transformareDFA(tranzitii,inchideri)

#AFISARE DFA
stari_finale=f.readline().split()
stari_finaleDFA=[]
g=open("outputDAF.out","w")
for cheie in dfa:
    for litera in dfa[cheie]:
        if dfa[cheie][litera]!=[]:
            g.write("{")
            for el in cheie:
                g.write(el+" ")
            g.write("} "+litera+" {")
            for el in dfa[cheie][litera]:
                g.write(el+" ")
            g.write("}\n")
for cheie in dfa:
    if isinstance(cheie,tuple):
        for el in cheie:
            if el in stari_finale and el not in stari_finaleDFA:
                stari_finaleDFA.append(cheie)
    elif cheie in stari_finale and cheie not in stari_finaleDFA:
        stari_finaleDFA.append(cheie)

for staref in stari_finaleDFA:
    print(staref)
    g.write("{")
    if isinstance(staref,tuple):
        for stare in staref:
            g.write(stare+" ")
    else:
        g.write(staref+" ")
    g.write("}")

