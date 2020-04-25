def check_combi(sombi):
    
    # fill smaller combinations with preceding zeros
    while len(sombi) < 4:
        sombi = "0" + sombi

    # positional values
    A = sombi[0]
    B = sombi[1]
    C = sombi[2]
    D = sombi[3]

    # digit counts
    zeros = sombi.count("0")
    ones = sombi.count("1")
    twos = sombi.count("2")
    threes = sombi.count("3")
    fours = sombi.count("4")
    fives = sombi.count("5")
    sixes = sombi.count("6")
    sevens = sombi.count("7")
    eights = sombi.count("8")
    nines = sombi.count("9")


    # 9285: One number is correct but wrong placed
    if not (
        ((nines!=0) and (twos==0) and (eights==0) and (fives==0) and A!="9")
        or
        ((nines==0) and (twos!=0) and (eights==0) and (fives==0) and B!="2")
        or
        ((nines==0) and (twos==0) and (eights!=0) and (fives==0) and C!="8")
        or
        ((nines==0) and (twos==0) and (eights==0) and (fives!=0) and D!="5")
        ): return False


    # 1937: Two numbers are correct but wrong placed
    if not (
        ((ones!=0) and (nines!=0) and (threes==0) and (sevens==0) and A!="1" and B!="9")
        or
        ((ones==0) and (nines==0) and (threes!=0) and (sevens!=0) and C!="3" and D!="7")
        or
        ((ones==0) and (nines!=0) and (threes!=0) and (sevens==0) and B!="9" and C!="3")
        or
        ((ones!=0) and (nines==0) and (threes==0) and (sevens!=0) and A!="1" and D!="7")
        or
        ((ones!=0) and (nines==0) and (threes!=0) and (sevens==0) and A!="1" and C!="3")
        or
        ((ones==0) and (nines!=0) and (threes==0) and (sevens!=0) and B!="9" and D!="7")
        ): return False


    # 5201 one number is right and well placed
    if not (
        ((A=="5") and (twos==0) and (zeros==0) and (ones==0))
        or
        ((fives==0) and (B=="2") and (zeros==0) and (ones==0))
        or
        ((fives==0) and (twos==0) and (C=="0") and (ones==0))
        or
        ((fives==0) and (twos==0) and (zeros==0) and (D=="1"))
        ): return False


    # 6507 Nothing is correct
    if not (
        (sixes==0) and (fives==0) and (zeros==0) and (sevens==0)
        ): return False


    # 8524 Two numers are correct but wrong placed
    if not (
        ((eights!=0) and (fives!=0) and (twos==0) and (fours==0) and A!="8" and B!="5")
        or
        ((eights==0) and (fives==0) and (twos!=0) and (fours!=0) and C!="2" and D!="4")
        or
        ((eights==0) and (fives!=0) and (twos!=0) and (fours==0) and B!="5" and C!="2")
        or
        ((eights!=0) and (fives==0) and (twos==0) and (fours!=0) and A!="8" and D!="4")
        or
        ((eights!=0) and (fives==0) and (twos!=0) and (fours==0) and A!="8" and C!="2")
        or
        ((eights==0) and (fives!=0) and (twos==0) and (fours!=0) and B!="5" and D!="4")
        ): return False

    # Otherwise
    return True


# Main function
if __name__ == "__main__":
    for combi in range(10000):
        sombi = str(combi)
        if check_combi(sombi):
            print("positive: " + sombi)


