import random as r

min_tiles = 7   # minimum number of tiles placed on the board
                # must be greater than the number of required resources

max_tiles = 12  # maximum number of tiles placed on the board
                # must be greater than the number of required resources

all_resources = ["Wood","Wood","Wood","Wood","Wheat","Wheat",
                 "Wheat","Wheat","Sheep","Sheep","Sheep","Sheep",
                 "Brick","Brick","Brick","Ore","Ore","Ore","Desert"]
required_resources = ['Wood', 'Wheat', 'Sheep', 'Brick', 'Ore']

chits = [2,3,3,4,4,5,5,6,6,7,8,8,9,9,10,10,11,11,12]

blank = '-'     # used for displaying parts of the map that have no tile on them

# helper function that places a resource (string) into one of the blank spots of the location (list of strings)
# blank spots are determined by comparing to blank, which is defined above
def place(resource, location):
    open_spots = []
    for i in range(len(location)):
        if location[i] == blank:
            open_spots.append(i)
    if open_spots == []:
        raise LookupError('Could not find an empty slot to place the resource.')
    location[r.choice(open_spots)] = resource
    return

def catan_randtiles():
    #todo: make a copy of the global resource list instead of mutating it directly.
    r.shuffle(chits)
    all_tiles = [blank for _ in all_resources]
    num_tiles = r.randint(min_tiles, max_tiles)


    # add all the required resources, and then decrement the number of tiles we need to add
    for reso in required_resources:
        # might want to add error checking here to make sure that all_resources actually contains reso to begin with
        all_resources.remove(reso)
        place(reso, all_tiles)
    num_tiles -= len(required_resources)

    for _ in range(num_tiles):
        reso = r.choice(all_resources)
        all_resources.remove(reso)
        place(reso, all_tiles)

    # for python 2.7
    print all_tiles[:3], "\n", all_tiles[3:7], "\n", all_tiles[7:12], "\n", all_tiles[12:16], "\n", all_tiles[16:19]
    print "\nNumbers:"
    print chits[:3], "\n", chits[3:7], "\n", chits[7:12], "\n", chits[12:16], "\n", chits[16:19]

    # for python 3
    #print(all_tiles[:3], "\n", all_tiles[3:7], "\n", all_tiles[7:12], "\n", all_tiles[12:16], "\n", all_tiles[16:19])
    # print(" ")
    # print("Numbers:")
    # print(chits[:3], "\n", chits[3:7], "\n", chits[7:12], "\n", chits[12:16], "\n", chits[16:19])



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

