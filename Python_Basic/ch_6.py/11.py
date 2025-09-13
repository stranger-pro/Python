import random as rd
i=1
while(i==1):
    DreamT = []

    wk_team = [1,2]
    A_team = [3,4,5,6,7]
    bo_team = [8,9,10,11,12,13,14,15]
    ba_team = [16,17,18,19,20,21,22]

    num_wk = rd.randint(1,2)
    num_ba = rd.randint(2,5)
    num_bo = rd.randint(2,5)
    num_A = 11 - ( num_ba + num_bo + num_wk )

    if(num_A==-1):
        num_A+=1
        if(num_wk == 2):
            num_wk-=1
        else:
            num_bo-=1

    if(num_A == 0):
        if(num_ba < num_bo):
            num_bo -= 1
            num_A += 1
        elif(num_ba > num_bo):
            num_ba -= 1
            num_A += 1
        else:
            num_bo -= 1
            num_ba -= 1
            num_A += 2

    if(num_A >=3):
        if(num_A >=5):
            num_A -= 2
            num_bo += 1
            num_ba += 1

        if(num_ba > num_bo):
            num_bo += 1
            num_A -= 1
        elif(num_ba < num_bo):
            num_ba += 1
            num_A -= 1
        else:
            num_bo += 1
            num_ba += 1
            num_A -= 2
    print()
    print(num_wk  , num_ba, num_bo, num_A)

    player = rd.sample(wk_team,num_wk)
    DreamT.extend(player)

    player = rd.sample(ba_team,num_ba)
    DreamT.extend(player)

    player = rd.sample(bo_team,num_bo)
    DreamT.extend(player)

    player = rd.sample(A_team,num_A)
    DreamT.extend(player)

    king = rd.sample(DreamT,2)

    ok = {
        'captain' : king[0],
        'v captain' : king[1]
    }

    print(DreamT)
    print(ok)
    i = int(input('Enter A num : '))
    print()

