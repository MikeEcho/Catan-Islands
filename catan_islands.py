import random as r

min_tiles = 7
max_tiles = 12
blank = '-'

def catan_randtiles():
    all_resources = ["Wood","Wood","Wood","Wood","Wheat","Wheat","Wheat","Wheat","Sheep","Sheep","Sheep","Sheep","Brick","Brick","Brick","Ore","Ore","Ore","Desert"]
    #random.shuffle(resources) # don't need this shit

    #numberlist = [2,3,3,4,4,5,5,6,6,7,8,8,9,9,10,10,11,11,12]
    #random.shuffle(numberlist) # ditto

    all_tiles = [blank for _ in all_resources]

    num_tiles = r.randint(min_tiles, max_tiles)

    required_resources = ['Wood', 'Wheat', 'Sheep', 'Brick', 'Ore']

    # add all the required resources, and then decrement the number of tiles we need to add
    # todo: factor out place_random to place in a random spot as a function
    # todo: also make it so we pick out of the remaining spots to avoid nonterminating condition
    for reso in required_resources:
        i = r.randint(0, len(all_tiles) - 1)
        while not all_tiles[i] == blank:
            i = r.randint(0, len(all_tiles))
        all_tiles[i] = reso
        all_resources.remove(reso)
    num_tiles -= len(required_resources)

    for _ in range(num_tiles):
        reso = r.choice(all_resources)
        i = r.randint(0, len(all_tiles) - 1)
        while not all_tiles[i] == blank:
            i = r.randint(0, len(all_tiles))
        all_tiles[i] = reso
        all_resources.remove(reso)

    print all_tiles[:3], "\n", all_tiles[3:7], "\n", all_tiles[7:12], "\n", all_tiles[12:16], "\n", all_tiles[16:19]
    #print(all_tiles[:3], "\n", all_tiles[3:7], "\n", all_tiles[7:12], "\n", all_tiles[12:16], "\n", all_tiles[16:19])
    print(" ")
    #print("Numbers:")
    #print(numberlist[:3], "\n", numberlist[3:7], "\n", numberlist[7:12], "\n", numberlist[12:16], "\n", numberlist[16:19])


print("Catan Islands v1.6")
print("Each bridge is one road length, and costs two roads")
print("Setup follows traditional Catan board 3-4-5-4-3 configuration")
print(" ")
print("Tiles:")
catan_randtiles()
print(" ")
print("If 7/robber is on a resource, replace with 6 or 8.")
print("If there exists a 6 already, place an 8. The same, vice versa.")
print("If there exist one 6 and one 8 already, roll for another 6 or 8.")
print("If there exist all 6 and 8s already, place 5 or 9 in similar fashion.")

