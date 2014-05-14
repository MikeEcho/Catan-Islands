import random

def catan_randtiles():
    resources = ["Wood","Wood","Wood","Wood","Wheat","Wheat","Wheat","Wheat","Sheep","Sheep","Sheep","Sheep","Brick","Brick","Brick","Ore","Ore","Ore","Desert"]
    random.shuffle(resources)

    numberlist = [2,3,3,4,4,5,5,6,6,7,8,8,9,9,10,10,11,11,12]
    random.shuffle(numberlist)

    dennis = 0
    for i in resources:
        nuke = random.randint(0,1)
        if nuke == 1:
            resources[dennis] = '-'
            numberlist[dennis] = '-'
        dennis += 1
    all_tiles = resources
    numbers = numberlist

    #to count nuked tiles
    nuke_counter = 0
    for i in all_tiles:
        if i == '-':
            nuke_counter += 1

    #to count remaining red numbers (6 and 8)
    red_counter = 0
    for j in numbers:
        if j == 6 or j==8:
            red_counter += 1

    #parameter checks: 1) need more than seven omitted tiles; 2) more than two red numbers; 3) at least one of each resource
    if (("Wood" in all_tiles) or ("Wheat" in all_tiles) or ("Sheep" in all_tiles) or ("Brick" in all_tiles) or ("Ore" in all_tiles) == False) or (nuke_counter <= 7) or (red_counter <= 2):
        catan_randtiles()
    else:
        print(resources[:3], "\n", resources[3:7], "\n", resources[7:12], "\n", resources[12:16], "\n", resources[16:19])
        print(" ")
        print("Numbers:")
        print(numberlist[:3], "\n", numberlist[3:7], "\n", numberlist[7:12], "\n", numberlist[12:16], "\n", numberlist[16:19])


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
print(" ")
print("--Update history--")
print("v1.1: tiles represented by numbers to denote any resource; numbers same format")
print("v1.2: replaced tile numbers by resource names")
print("v1.3: implemented limit of 7 on number of omitted tiles")
print("v1.4: implemented base requirement of one of each resource on the board")
print("v1.5: modified numbers display to see remaining numbers clearly")
print("v1.6: implemented base requirement of at least three red numbers")
