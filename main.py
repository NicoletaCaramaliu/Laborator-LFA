"""def verificare(cuv):
    f=open("cuvant.in","r")
    g=open("cuvant.out","w")
    drum={("q0"):[]}
    i=1
    stari_curente={"q0"}
    drum_litera={}
    n=int(f.readline())

    for i in range(n):
        qi,l,qf=f.readline().split()
        if (qi,l) not in drum_litera:
            drum_litera[(qi,l)]=[qf]
        else:
            drum_litera[(qi,l)].append(qf)
    stari_finale=f.readline().split()
    print(stari_finale)
    print(drum_litera)
    for i in range(len(cuv)):
        for t in drum_litera:
            if cuv[i] in t:
                if t[0] in stari_curente:

                    stari_curente=drum_litera[t]
    ok=0
    for stare in stari_finale:
        if stare in drum[-1]:
            ok=1
    print(drum,ok)"""

drum=[]
verif = False
def verificare(cuv,st_act,st_fin,tranzitii):
    global verif
    drum.append(st_act)
    if cuv=="":
        if st_act in st_fin:
            g.write("Cuvantul este acceptat\nDrumul parcurs de acesta este ")
            for d in drum:
                g.write("->"+d)
            g.write("\n\n")
            verif = True
    elif cuv[0] in tranzitii:
        for stare in tranzitii[cuv[0]]:
            if stare[0]==st_act:
                verificare(cuv[1:],stare[1],st_fin,tranzitii)



f = open("cuvant.in", "r")
g = open("cuvant.out", "w")
tranzitii = {}
n = int(f.readline())
stare_actuala = f.readline().strip()

for _ in range(n):
    qi, l, qf = f.readline().split()
    if l not in tranzitii:
        tranzitii[l]=[(qi, qf)]
    else:
        tranzitii[l].append((qi,qf))


stari_finale=f.readline().split()
cuvinte=f.readline().split()
for cuvant in cuvinte:
    verif = False
    copie=stare_actuala
    verificare(cuvant,copie,stari_finale,tranzitii)
    if verif == False:
        g.write("Neacceptat\n\n")

