import time
start_time=time.time()
minMana=999999

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
    global minMana
    for i in range(5):
        manaCost,myHP,myMana,hisHP,sT,pT,rT=args
        
        pT,rT,sT,hisHP,myMana=applyEffects(pT,rT,sT,hisHP,myMana)

        #uncomment the following for part 2
        #myHP-=1
        #if myHP<=0:
        #   continue
        
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
        if manaCost>=minMana:
            continue

        pT,rT,sT,hisHP,myMana=applyEffects(pT,rT,sT,hisHP,myMana)

        myHP-=9-((sT>0)*7)
        
        if hisHP<=0:
            minMana=min(minMana,manaCost)
            continue
        elif myHP<=0:
            continue

        simulate(manaCost,myHP,myMana,hisHP,sT,pT,rT)

simulate(0,50,500,51,0,0,0)
print minMana
print time.time()-start_time
# 900-03403200
#1216-31432430
