def profitFinder(A1, A2, costA1, costA2):
    # inititalize B
    B1=4
    B2=8
    costB1=5
    costB2=5

    # initialize variables
    t=1000000
    profitSumA1=0
    profitSumA2=0

    # range 0, 1mil
    from random import randrange
    for i in range(0,t):
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

        #compare with coin toss & decide
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
        else:
            pickB1 = 0

        pickB2 = 0
        if coinToss> (pChooseA1+pChooseA2+pChooseB1):
            pickB2 = 1
        else:
            pickB2 = 0

    # calculate profit per
    profPerA1=profitSumA1/t
    profPerA2=profitSumA2/t

    #outputs
    return t, profPerA2, profPerA1



if __name__=="__main__":
    #heres where you change the variables
    A1 = 4
    A2 = 6
    costA1 = 4
    costA2 = 3

    from random import randrange
    for i in range(100):
        #initialize lists for maximums
        A1list=[]
        A2list=[]
        A1costList=[]
        A2costList=[]
        profitlistA1=[]
        profitlistA2=[]

    #try random values
        A1=randrange(0,11)
        A2=randrange(0,11)
        costA1=randrange(200,700,1)*.01
        costA2=randrange(200,700,1)*.01


#make lists so we can get the max
        A1list.append(A1)
        A2list.append(A2)
        A1costList.append(costA1)
        A2costList.append(costA2)



# create prof lists
        t, profPerA2, profPerA1 = profitFinder(A1, A2, costA1, costA2)

        profitlistA1.append(profPerA1)
        profitlistA2.append(profPerA2)
        maxprofitlist=[]
        maxprofitlist.append(profPerA1+profPerA2)
        maxProfit=max(maxprofitlist)
        maxposition=maxprofitlist.index(maxProfit)



# print maximums

print()
print("Trials: ", t)
print("Max profit per person (A1): ", profitlistA1[maxposition])
print()
print("Max profit per person (A2): ", profitlistA2[maxposition])
print("A1 max= ", A1list[maxposition], "A2 max= ", A2list[maxposition], "Best cost A1= ", A1costList[maxposition], "Best cost A2= ", A2costList[maxposition])