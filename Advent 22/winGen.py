#winGen.py bossHP bossDamage
import sys,copy,itertools
bossHP,bossDamage=int(sys.argv[1]),int(sys.argv[2])
bossReducedDamage=max(bossDamage-7,1)
moveSequence=[]

def applyEffects(poisonTimer,rechargeTimer,shieldTimer,bossHP,myMana):
    if poisonTimer>0:
        poisonTimer-=1
        bossHP-=3
        
    if rechargeTimer>0:
        rechargeTimer-=1
        myMana+=101
        
    if shieldTimer>0:
        shieldTimer-=1
        
    return list([poisonTimer,rechargeTimer,shieldTimer,bossHP,myMana])

def simulate(*args):
    global minMana,bossDamage,bossReducedDamage,moveSequence,part1
    
    for i in range(5):
        manaCost,myHP,myMana,bossHP,shieldTimer, \
            poisonTimer,rechargeTimer=args
        
        poisonTimer,rechargeTimer,shieldTimer,bossHP,myMana= \
            applyEffects(poisonTimer,rechargeTimer,shieldTimer,bossHP,myMana)

        if not part1:
            myHP-=1
            if myHP<=0:
               continue
        
        currentSpellMana=(53,73,113,173,229)[i]
        currentSpellTimer=(0,0,shieldTimer,poisonTimer,rechargeTimer)[i]
        
        if myMana<currentSpellMana or currentSpellTimer!=0:
            continue

        if i==0:
            bossHP-=4
        elif i==1:
            bossHP-=2
            myHP+=2
        elif i==2:
            shieldTimer=6
        elif i==3:
            poisonTimer=6
        elif i==4:
            rechargeTimer=5

        myMana-=currentSpellMana
        manaCost+=currentSpellMana
        
        if manaCost>minMana:
            continue

        poisonTimer,rechargeTimer,shieldTimer,bossHP,myMana= \
            applyEffects(poisonTimer,rechargeTimer,shieldTimer,bossHP,myMana)

        myHP-=(bossDamage,bossReducedDamage)[shieldTimer>0]

        if bossHP<=0:
            if part1:
                winners.append(("".join(list(str(j) for j in moveSequence))+str(i),manaCost))
            else:
                winners.append(("".join(list(str(j) for j in moveSequence))+str(i),manaCost))
            
            minMana=min(minMana,manaCost)
            continue
        elif myHP<=0:
            continue

        moveSequence.append(i)
        simulate(manaCost,myHP,myMana,bossHP,shieldTimer,poisonTimer,rechargeTimer)
        moveSequence.pop()

winners,minMana,part1=[],sys.maxint,True
simulate(0,50,500,bossHP,0,0,0)
print "Part 1 solution - "+str(minMana)+"\nMove sequences for \"winPrint.py "+str(bossHP)+" "+str(bossDamage)+" moveSequence 1\":"
for i in itertools.ifilter(lambda x: x[1]==minMana,winners):
    print i[0]

winners,minMana,part1=[],sys.maxint,False
simulate(0,50,500,bossHP,0,0,0)
print "\nPart 2 solution - "+str(minMana)+"\nMove sequences for \"winPrint.py "+str(bossHP)+" "+str(bossDamage)+" moveSequence 2\":"
for i in itertools.ifilter(lambda x: x[1]==minMana,winners):
    print i[0]
