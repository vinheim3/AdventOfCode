#winGen.py bossHP bossDamage
import sys,copy
hisHP,hisDam=int(sys.argv[1]),int(sys.argv[2])
hisRDam=max(hisDam-7,1)

def applyEffects(pT,rT,sT,hisHP,myMana):
    if pT>0:
        pT-=1
        hisHP-=3
    if rT>0:
        rT-=1
        myMana+=101
    if sT>0:
        sT-=1
    return list([pT,rT,sT,hisHP,myMana])

def simulate(*args):
    global minMana,hisDam,x,y,hisRDam
    for i in range(5):
        manaCost,myHP,myMana,hisHP,sT,pT,rT,part2,seq=args[1:]

        L=[]
        if seq:
            L=copy.deepcopy(args[0])
            L.append(i)
        
        pT,rT,sT,hisHP,myMana=applyEffects(pT,rT,sT,hisHP,myMana)

        if part2:
            myHP-=1
            if myHP<=0:
               continue
        
        cm=(53,73,113,173,229)[i]
        cond=(0,0,sT,pT,rT)[i]
        
        if myMana<cm or cond!=0:
            continue

        if i==0:
            hisHP-=4
        elif i==1:
            hisHP-=2
            myHP+=2
        elif i==2:
            sT=6
        elif i==3:
            pT=6
        elif i==4:
            rT=5

        myMana-=cm
        manaCost+=cm
        if not seq and manaCost>=minMana:
            continue
        if seq and manaCost>minMana:
            continue

        pT,rT,sT,hisHP,myMana=applyEffects(pT,rT,sT,hisHP,myMana)

        myHP-=(hisDam,hisRDam)[sT>0]
        
        if hisHP<=0:
            if seq:
                if not part2 and manaCost==x:
                    print "".join(list(str(i) for i in L))
                if part2 and manaCost==y:
                    print "".join(list(str(i) for i in L))
            minMana=min(minMana,manaCost)
            continue
        elif myHP<=0:
            continue

        simulate(L,manaCost,myHP,myMana,hisHP,sT,pT,rT,part2,seq)

minMana=9999
simulate([],0,50,500,hisHP,0,0,0,False,False)
x=minMana
print "Part 1 solution - "+str(x)+"\nMove sequences for \"winPrint.py "+str(hisHP)+" "+str(hisDam)+" moveSequence 1\":"
minMana=9999
simulate([],0,50,500,hisHP,0,0,0,False,True)

minMana=9999
simulate([],0,50,500,hisHP,0,0,0,True,False)
y=minMana
print "\nPart 2 solution - "+str(y)+"\nMove sequences for \"winPrint.py "+str(hisHP)+" "+str(hisDam)+" moveSequence 2\":"
minMana=9999
simulate([],0,50,500,hisHP,0,0,0,True,True)
