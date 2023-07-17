import random
def play():
    l=[]
    A='A'
    a='a'
    for i in range(97,123):
        l.append(chr(i))
    for i in range(65,91):
        l.append(chr(i))
    print("\n",l)
    r=random.choice(l)
    
    count=0
    for i in range(66,91):
        A+=chr(i)
    for i in range(98,123):
        a+=chr(i)
    
    while True:
        count+=1        
        inp=(input("\n\t\t\tGuess The Letter :"))
        if inp==r:
            print("\n\t\t\tYou Found!!!")
            break
        if r in A:
            if inp in A:
                if ascii(inp)>ascii(r):
                    print("\n\t\t\tToo High")
                else:
                    print("\n\t\t\tToo Low")
            elif inp in a:
                if ascii(inp)>ascii(r):
                    print("\n\t\t\tToo Low")
                else:
                    print("\n\t\t\tToo High")
        elif r in a:
            if inp in A:
                if ascii(inp)<ascii(r):
                    print("\n\t\t\tToo High")
                else:
                    print("\n\t\t\tToo Low")
            if inp in a:
                if ascii(inp)>ascii(r):
                    print("\n\t\t\tToo High")
                else:
                    print("\n\t\t\tToo Low")
    print("\n\t\t\tTotal No Of Tries :",count)
    print("\n\t\t________________________________")
    return count

a=[]
A=[]
for i in range(65,91):
    A.append(chr(i))
for i in range(97,123):
    a.append(chr(i))
no=(input("\t\t\tEnter the no of players : "))
if no in (A or a):
    print("Invalid input")
    quit()
else:
    no=int(no)
    players_counts=[]
    cou=[]
    players=[]

    for i in range(1,no+1):
        print("\n\t\t\tEnter Player",i)
        players.append(input("\t\t\tName : "))

    for i in range(1,no+1):
        print("\n\t\t\tYou Are Player : ",i)
        c=play()
        counts={i:c}
        players_counts.append(counts)
        cou.append(c)
        
    cou2=cou.copy()
    rank=players.copy()
    index=cou.index(min(cou))
    rep=cou.count(min(cou))
    all_rep=[]

    for x in cou:
        if cou.count(x)>1:
            all_rep.append(x)
            
    print("\n\t\t   {Players : Tries} -",players_counts)

    def rep_f():
        rep_name=[]
        rep_count=[]
        rep_playercount=[]
        print("\n\t \"Only the players who got tied with minimum no of tries should continue\"")
            
        for i in range(1,rep+1):
            rep_name.append(input("\n\t\t\tEnter Your Name : "))
            rep_c=play()
            rep_counts={i:rep_c}
            rep_playercount.append(rep_counts)
            rep_count.append(rep_c)
            rep_count2=rep_count.copy()
            rep_name2=rep_name.copy()
        all_repeated=[]
        min_repeated=rep_count.count(min(rep_count))
        if min_repeated>1:
            rep_f()
        for x in rep_count:
            if rep_count.count(x)>1:
                all_repeated.append(x)
        if all_repeated==[]:
            print("\n\t\t   {Player : Tries}",rep_playercount,"\n")
            rep_index=rep_count.index(min(rep_count))
            if len(rep_name)>2:
                j=1
                while j<=len(rep_name):            
                    print("\n\t\t\tPosition",j,"is : ",rep_name2[index])
                    j+=1
                    del rep_count2[index]
                    del rep_name2[index]
                    if len(cou2)>0 :
                            rep_index=rep_count2.index(min(rep_count))
                    else:
                        break
            
            else:    
                    rep_index=rep_count.index(min(rep_count))
                    print("\n\t\t\tWinner is :",rep_name[rep_index])
    if rep>1:
        rep_f()
            
    elif all_rep==[]:
        if no>2:
            j=1
            while j<=no:            
                print("\n\t\t\tPosition",j,"is : ",rank[index])
                j+=1
                del cou2[index]
                del rank[index]
                if len(cou2)>0 :
                    index=cou2.index(min(cou2))
                else:
                    break
        else:
            index=cou2.index(min(cou2))
            print("\n\t\t\t",rank[index],"Is the winner")
            
    else:
        index=cou2.index(min(cou2))
        print("\n\t\t\t",rank[index],"Is the winner")
    
        
    
    
    
    


