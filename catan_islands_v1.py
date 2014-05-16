import random as r

def catan_islands():
    base_tiles = ["Wood","Wheat","Sheep","Brick","Ore"] #always on board
    misc_tiles = ["Wood","Wood","Wood","Wheat","Wheat","Wheat",
                 "Sheep","Sheep","Sheep","Brick","Brick","Ore","Ore"] #tiles which maybe taken out

    misc_num = [2,3,3,4,4,5,5,6,8,9,9,10,10,11,11,12] #numbers which maybe taken out
    base_num = [6,8] #following code to ensure at least three red numbers on board
    a = r.choice(base_num)
    base_num.append(a)
    del misc_num[misc_num.index(a)]
    #finish building base lists
    for i in range(2):
        b = r.choice(misc_num)
        base_num.append(b)
        del misc_num[misc_num.index(b)]
    base_tiles += ["Desert"]
    base_num += [7]
    #appending base tiles/numbers to their respective global lists
    all_tiles = []
    all_num = []
    all_tiles += base_tiles
    all_num += base_num
    #nuking/island formation stage
    counter = 0
    nuke_counter = 0
    for i,j in zip(misc_tiles,misc_num):
        nuke = r.randint(0,1)
        if nuke == 1:
            misc_tiles[counter] = '-'
            misc_num[counter] = '-'
            nuke_counter += 1
        counter += 1
    all_tiles += misc_tiles
    all_num += misc_num
    #adding nuked misc lists to their respective global lists
    alltiles_shuf = []
    allnum_shuf = []
    #shuffling the two lists while keeping tile-number correspondences in their places
    index_shuf = list(range(len(all_tiles)))
    r.shuffle(index_shuf)
    for i in index_shuf:
        alltiles_shuf.append(all_tiles[i])
        allnum_shuf.append(all_num[i])
    #condition for at least nine empty spaces to encourage island formation
    if (nuke_counter < 9):
        catan_islands()
    else:
        print("Catan Islands v1.7")
        print("Each bridge is one road length, and costs two roads")
        print("Setup follows traditional Catan board 3-4-5-4-3 configuration")
        print(" ")
        print("Tiles:")
        print(alltiles_shuf[:3], "\n", alltiles_shuf[3:7], "\n", alltiles_shuf[7:12],
              "\n", alltiles_shuf[12:16], "\n", alltiles_shuf[16:19])
        print(" ")
        print("Numbers:")
        print(allnum_shuf[:3], "\n", allnum_shuf[3:7], "\n", allnum_shuf[7:12],
              "\n", allnum_shuf[12:16], "\n", allnum_shuf[16:19])
        print(" ")
        print("Update history can be found on www.github.com/MikeEcho/Catan-Islands")

catan_islands()
