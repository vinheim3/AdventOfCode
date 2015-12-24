#winPrint.py bossHP bossDamage winningMoveSequence part1or2
import sys
data,part=sys.argv[3:]
myHP,myMana,hisHP,hisDam,sT,pT,rT=50,500,int(sys.argv[1]),int(sys.argv[2]),0,0,0
max1=hisDam<=7

def printTurn(player):
    global myHP,sT,myMana,hisHP
    print "-- "+player+" turn --"
    print "- Player has "+str(myHP)+" hit points, "+str((sT>0)*7)+" armor, "+str(myMana)+" mana"
    print "- Boss has "+str(hisHP)+" hit points"

def applyEffects():
    global sT,pT,rT,hisHP,myMana
    if sT>0:
        sT-=1
        print "Shield's timer is now "+str(sT)+"."
        if sT==0:
            print "Shield wears off, decreasing armor by 7"
    if pT>0:
        pT-=1
        hisHP-=3
        print "Poison deals 3 damage"+(". This kills the boss, and the player wins.","; its timer is now "+str(pT)+".")[hisHP>0]
        if hisHP<=0:
            sys.exit()
        if pT==0:
            print "Poison wears off."
    if rT>0:
        rT-=1
        myMana+=101
        print "Recharge provides 101 mana; its timer is now "+str(rT)+"."
        if rT==0:
            print "Recharge wears off."

for i in data:
    printTurn("Player")

    if part=="2":
        myHP-=1
        print "Player loses 1 hit point due to weakness."
    
    applyEffects()
    
    if i=="0":
        myMana-=53
        hisHP-=4
        print "Player casts Magic Missile, dealing 4 damage."+(" This kills the boss, and the player wins.","")[hisHP>0]
    elif i=="1":
        myMana-=73
        hisHP-=2
        myHP+=2
        print "Player casts Drain, dealing 2 damage, and healing 2 hit points."+(" This kills the boss, and the player wins.","")[hisHP>0]
    elif i=="2":
        myMana-=113
        sT=6
        print "Player casts Shield, increasing armor by 7."
    elif i=="3":
        myMana-=173
        pT=6
        print "Player casts Poison."
    elif i=="4":
        myMana-=229
        rT=5
        print "Player casts Recharge."
    if hisHP<=0:
        sys.exit()

    print ""
    printTurn("Boss")
    applyEffects()
    myHP-=hisDam-((sT>0)*7)
    print "Boss attacks for "+str(hisDam)+(""," - 7 ="+("",">")[max1]+" "+str(max(hisDam-7,1)))[sT>0]+" damage!\n"
