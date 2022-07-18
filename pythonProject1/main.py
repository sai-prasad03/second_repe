n = [["saiprasad",65],["prachi",45],["praveena",70],["pratik",50],["samarth",60],["sidharth",82],["rudra",40]]
for name,rank in n:
    if rank >70:
        print(name,"scored",rank)
    elif rank == 65:
        print(name,"highest mark is",rank)
    elif rank<50:
        (name,"have to be good performence in next sem")
    elif rank>80:
        print(name,"has first number in class with rank",rank)