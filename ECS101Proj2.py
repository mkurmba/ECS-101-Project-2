B1=4
B2=8
costB1=5
costB2=5

# can change these shits
A1=4
A2=6
costA1=4
costA2=3


if __name__=="__main__":
    profitSumA1=0
    profitSumA2=0
    profitA1=0
    profitA2=0
    from random import randrange
    for i in range(0,50000):
        randomPlacement=randrange(0,1000)*.01
        distfromcustomerA1= abs(randomPlacement-A1)
        distfromcustomerA2 = abs(randomPlacement - A2)
        distfromcustomerB1 = abs(randomPlacement - B1)
        distfromcustomerB2 = abs(randomPlacement - B2)
    # scores
        scoreA1=(10-(distfromcustomerA1))+3*(6-costA1)
        scoreA2=(10-(distfromcustomerA2))+3*(6-costA2)
        scoreB1=(10-(distfromcustomerB1))+3*(6-costB1)
        scoreB2=(10-(distfromcustomerB2))+3*(6-costB2)

        pChooseA1 = scoreA1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        pChooseA2 = scoreA2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        pChooseB1 = scoreB1 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)
        pChooseB2 = scoreB2 / (scoreA1 + scoreA2 + scoreB1 + scoreB2)

        coinToss=randrange(0,1001)*.001

        pickA1=0
        if coinToss<= pChooseA1:
            pickA1=1
            profitA1=(costA1-2)
            profitSumA1 = profitA1 + profitSumA1
        else:
            pickA1=0

        pickA2 = 0
        if coinToss > pChooseA1 and coinToss< (pChooseA1+pChooseA2):
            pickA2 = 1
            profitA2=(costA2-2)
            profitSumA2 = profitA2 + profitSumA2
        else:
            pickA2 = 0

        pickB1 = 0
        if coinToss >= (pChooseA1+pChooseA2) and coinToss< (pChooseA1+pChooseA2+pChooseB1):
            pickB1 = 1
            profitA1=0
            profitA2=0
        else:
            pickB1 = 0

        pickB2 = 0
        if coinToss> (pChooseA1+pChooseA2+pChooseB1):
            pickB2 = 1
            profitA1=0
            profitA2=0
        else:
            pickB2 = 0
        print()
        print(pickA1)
        print(pickA2)
        print(pickB1)
        print(pickB2)



    profPerA1=profitSumA1/50000
    profPerA2=profitSumA2/50000

    print(profitSumA1)
    print(profPerA1)
    print()
    print(profitSumA2)
    print(profPerA2)