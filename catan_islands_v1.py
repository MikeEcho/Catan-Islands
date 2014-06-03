import random as r
from itertools import count


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
    def nuke(misc_tiles, misc_num):
        counter = 0
        nuke_counter = 0
        for i,j in zip(misc_tiles,misc_num):
            nuke_num = r.randint(0,1)
            if nuke_num == 1:
                misc_tiles[counter] = '-'
                misc_num[counter] = '-'
                nuke_counter += 1
            counter += 1
        if nuke_counter < 7:
            nuke(misc_tiles, misc_num)
        else:
            return misc_tiles, misc_num
    nuke(misc_tiles, misc_num)
    #adding nuked misc lists to their respective global lists
    all_tiles += misc_tiles
    all_num += misc_num
    #shuffling the two lists while keeping tile-number correspondences in their places
    alltiles_shuf = []
    allnum_shuf = []
    index_shuf = list(range(len(all_tiles)))
    r.shuffle(index_shuf)
    for i in index_shuf:
        alltiles_shuf.append(all_tiles[i])
        allnum_shuf.append(all_num[i])

    def ports(alltiles_shuf):
        #possible tile intersection sides with other tiles defined first, clockwise from west to south west
        t = alltiles_shuf
        t_intersects = [[t[0], ['-','-','-',t[1],t[4],t[3]]], [t[1], [t[0],'-','-',t[2],t[5],t[4]]], [t[2], [t[1],'-','-','-',t[6],t[5]]],
                        [t[3], ['-','-',t[0],t[4],t[8],t[7]]], [t[4], [t[3],t[0],t[1],t[5],t[9],t[8]]], [t[5], [t[4],t[1],t[2],t[6],t[10],t[9]]],
                        [t[6], [t[5],t[2],'-','-',t[11],t[10]]], [t[7], ['-','-',t[3],t[8],t[12],'-']], [t[8], [t[7],t[3],t[4],t[9],t[13],t[12]]],
                        [t[9], [t[8],t[4],t[5],t[10],t[14],t[13]]], [t[10], [t[9],t[5],t[6],t[11],t[15],t[14]]], [t[11], [t[10],t[6],'-','-','-',t[15]]],
                        [t[12], ['-',t[7],t[8],t[13],t[16],'-']], [t[13], [t[12],t[8],t[9],t[14],t[17],t[16]]], [t[14], [t[13],t[9],t[10],t[15],t[18],t[17]]],
                        [t[15], [t[14],t[10],t[11],'-','-',t[18]]], [t[16], ['-',t[12],t[13],t[17],'-','-']], [t[17], [t[16],t[13],t[14],t[18],'-','-']],
                        [t[18], [t[17],t[14],t[15],'-','-','-']]
        ]
        t_existing_intersects = t_intersects
        i_counter = 0
        for intersect in t_existing_intersects[i_counter][1]:
            if intersect == '-':
                intersect = '-'
            i_counter += 1
        #coastline (open tile sides) counter, divided by the nine ports, gives spacing between each port
        #first count the inner sides which do not touch other tiles
        coastline = 0
        tile_counter = 0
        for tile in t_intersects:
            if t_intersects[tile_counter][0] == '-':
                tile_counter += 1
            elif t_intersects[tile_counter][0] != '-':
                for intersecting_tile in t_intersects[tile_counter][1]:
                    if intersecting_tile == '-':
                        coastline += 1
                tile_counter += 1
        #now we have a coastline count. We now divide by nine (the number of ports) to determine the spacing between each port
        #FYI the nine ports are: four 3:1 ports, and one of each resource 2:1 port
        port_spacing = coastline // 9

        compass = ['West','North West','North East','East','South East','South West']

        #creating a list of orientations by existing tile which can have a port (i.e. sides of an existing tile which are adjacent to other tiles)
        possible_ports = t_existing_intersects[:]
        for side in possible_ports:
            if side[0] != '-':
                for index, value in enumerate(side[1]):
                    if value == '-':
                        side[1][index] = compass[index]
                    if value != '-':
                        side[1][index] = '-'
            elif side[0] == '-':
                for index, value in enumerate(side[1]):
                    side[1][index] = '-'
        #getting rid of '-' elements
        for tile in possible_ports:
            for portside in tile[1]:
                tile[1] = [portside for portside in tile[1] if portside != '-']
        #using port spacing to pick ports
        c = count()
        chosen_ports = [[resource, [side for side in sides if next(c) % port_spacing == 0]] for resource, sides in possible_ports]
        all_ports = ['Wood 2:1','3:1','Wheat 2:1','3:1','Sheep 2:1','3:1','Brick 2:1','3:1','Ore 2:1']

        row1,row2,row3,row4,row5 = dict(chosen_ports[:3]),dict(chosen_ports[3:7]),dict(chosen_ports[7:12]),\
                                   dict(chosen_ports[12:16]),dict(chosen_ports[16:19])

        # placed_ports = [res, [side + ":" + port for (side,port) in (sides,all_ports) while len(all_ports)>0] for res, sides in chosen_ports]
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        print(row5)
    print(" ")

    print("Catan Islands v1.8. Based on The Settlers of Catan board game.")
    print("Each bridge is one road length, and costs two roads")
    print("Setup follows traditional Catan board 3-4-5-4-3 configuration")
    print(" ")
    print("Tiles:")
    print(alltiles_shuf[:3], "\n", alltiles_shuf[3:7], "\n", alltiles_shuf[7:12],
          "\n", alltiles_shuf[12:16], "\n", alltiles_shuf[16:19])
    print(" ")
    print("Ports:")
    str(ports(alltiles_shuf))
    print(" ")
    print("Numbers:")
    print(allnum_shuf[:3], "\n", allnum_shuf[3:7], "\n", allnum_shuf[7:12],
          "\n", allnum_shuf[12:16], "\n", allnum_shuf[16:19])
    print(" ")
    print("Update history can be found on www.github.com/MikeEcho/Catan-Islands")

catan_islands()
