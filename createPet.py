import math

categories = ["strawberry", "angora", "axolotl", "seaCucumber", "gown", \
              "persianCat", "hoopskirt", "acorn", "siameseCat", "bathTowel",\
              "dough", "coffeepot", "screen"]
catNums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

speciesDict = { "sp0" : {0 : 0.0, 1 : 0.4168, 2 : 0.0, 3 : 0.0, 4 : 0.0, 5 : 0.0, \
        6 : 0.0, 7 : 0.3627, 8 : 0.0, 9 : 0.0, 10 : 0.0, 11 : 0.2204, 12 : 0.0}, \
            "sp1" : {0 : 0.0, 1 : 0.0, 2 : 0.0, 3 : 0.0, 4 : 0.0, 5 : 0.0, 6 : 0.0, \
                    7 : 0.0, 8 : 0.4653, 9 : 0.1126, 10 : 0.4220, 11 : 0.0, 12 : 0.0}, \
            "sp2" : {0 : 0.2211, 1 : 0.5834, 2 : 0.2210, 3 : 0.3520, 4 : 0.6617, 5 : 0.0, \
                    6 : 0.0, 7 : 0.0, 8 : 0.0, 9 : 0.0, 10 : 0.0, 11 : 0.0, 12 : 0.0}, \
            "sp3" : {0 : 0.6232, 1 : 0.3228, 2 : 0.2781, 3 : 0.3463, 4 : 0.5567, 5 : 0.0, \
                    6 : 0.0, 7 : 0.0, 8 : 0.0, 9 : 0.0, 10 : 0.0, 11 : 0.0, 12 : 0.0}, \
            "sp4" : {0 : 0.4078, 1 : 0.6695, 2 : 0.3525, 3 : 0.2996, 4 : 0.4139, 5 : 0.0, \
                    6 : 0.0, 7 : 0.0, 8 : 0.0, 9 : 0.0, 10 : 0.0, 11 : 0.0, 12 : 0.0}, \
            "sp5" : {0 : 0.2668, 1 : 0.0, 2 : 0.6489, 3 : 0.5217, 4 : 0.0, 5 : 0.0, \
                    6 : 0.0, 7 : 0.0, 8 : 0.0, 9 : 0.0, 10 : 0.0, 11 : 0.0, 12 : 0.0}, \
            "sp6" : {0 : 0.2745, 1 : 0.0, 2 : 0.4341, 3 : 0.0, 4 : 0.0, 5 : 0.0, 6 : 0.0, \
                    7 : 0.0, 8 : 0.0, 9 : 0.0, 10 : 0.0, 11 : 0.0, 12 : 0.2392}, \
            "sp7" : {0 : 0.0, 1 : 0.0, 2 : 0.0, 3 : 0.0, 4 : 0.0, 5 : 0.6472, 6 : 0.1226, \
                    7 : 0.2300, 8 : 0.0, 9 : 0.0, 10 : 0.0, 11 : 0.0, 12 : 0.0}, \
            "sp8" : {0 : 0.6040, 1 : 0.0, 2 : 0.0, 3 : 0.0, 4 : 0.0, 5 : 0.0, \
                    6 : 0.0, 7 : 0.0, 8 : 0.6163, 9 : 0.4649, 10 : 0.0, 11 : 0.0, 12 : 0.0}, \
            "sp9" : {0 : 0.02526, 1 : 0.0412, 2 : 0.8562, 3 : 0.0, 4 : 0.0, 5 : 0.0, \
                    6 : 0.0, 7 : 0.0, 8 : 0.0, 9 : 0.1299, 10 : 0.4909, 11 : 0.0, 12 : 0.0}, \
            "sp10" : {0 : 0.2877, 1 : 0.3462, 2 : 0.3766, 3 : 0.2502, 4 : 0.3350, 5 : 0.1734, \
                    6 : 0.1476, 7 : 0.3780, 8 : 0.3612, 9 : 0.2625, 10 : 0.1453, \
                    11 : 0.2553, 12 : 0.0}, \
            "sp11" : {0 : 0.5088, 1 : 0.0, 2 : 0.2857, 3 : 0.0, 4 : 0.0, 5 : 0.1826, \
                    6 : 0.3388, 7 : 0.4121, 8 : 0.0744, 9 : 0.0, 10 : 0.3018, \
                    11 : 0.3444, 12 : 0.3206}, \
            "sp12" : {0 : 0.4048, 1 : 0.0, 2 : 0.2179, 3 : 0.0, 4 : 0.4246, 5 : 0.1645, \
                    6 : 0.2621, 7 : 0.3355, 8 : 0.4165, 9 : 0.0, 10 : 0.2330, \
                    11 : 0.3012, 12 : 0.2636}, \
            "sp13" : {0 : 0.2651, 1 : 0.5162, 2 : 0.1636, 3 : 0.0, 4 : 0.1927, 5 : 0.1172, \
                    6 : 0.1635, 7 : 0.2345, 8 : 0.3030, 9 : 0.0, 10 : 0.1461, \
                    11 : 0.2092, 12 : 0.5800}, \
            "sp14" : {0 : 0.1827, 1 : 0.1503, 2 : 0.1026, 3 : 0.0, 4 : 0.2086, 5 : 0.3700, \
                    6 : 0.0858, 7 : 0.0763, 8 : 0.4867, 9 : 0.0, 10 : 0.1155, \
                    11 : 0.4032, 12 : 0.5726}, \
            "sp15" : {0 : 0.0, 1 : 0.0, 2 : 0.0, 3 : 0.1171, 4 : 0.1871, 5 : 0.0, \
                    6 : 0.2775, 7 : 0.4116, 8 : 0.7399, 9 : 0.3046, 10 : 0.0, \
                    11 : 0.2284, 12 : 0.1107}, \
            "sp16" : {0 : 0.0, 1 : 0.0, 2 : 0.0, 3 : 0.1218, 4 : 0.1943, 5 : 0.0, \
                    6 : 0.2797, 7 : 0.4014, 8 : 0.7523, 9 : 0.8936, 10 : 0.0, \
                    11 : 0.1981, 12 : 0.0853}, \
            "sp17" : {0 : 0.0, 1 : 0.0, 2 : 0.3720, 3 : 0.0332, 4 : 0.0964, 5 : 0.0, \
                    6 : 0.1388, 7 : 0.1992, 8 : 0.6707, 9 : 0.4435, 10 : 0.0, \
                    11 : 0.0983, 12 : 0.3687}, \
            "sp18" : {0 : 0.5990, 1 : 0.0, 2 : 0.2483, 3 : 0.0, 4 : 0.0653, 5 : 0.0, \
                    6 : 0.1068, 7 : 0.1291, 8 : 0.6301, 9 : 0.2990, 10 : 0.0, \
                    11 : 0.0375, 12 : 0.2426}, \
            "sp19" : {0 : 0.3740, 1 : 0.0, 2 : 0.1575, 3 : 0.0, 4 : 0.0277, 5 : 0.5412, \
                    6 : 0.0787, 7 : 0.1454, 8 : 0.5653, 9 : 0.3751, 10 : 0.0, \
                    11 : 0.1708, 12 : 0.1569}, \
            "sp20" : {0 : 0.1108, 1 : 0.0, 2 : 0.0474, 3 : 0.3761, 4 : 0.2462, 5 : 0.4680, \
                    6 : 0.3205, 7 : 0.1382, 8 : 0.0, 9 : 0.2924, 10 : 0.3228, \
                    11 : 0.3030, 12 : 0.4008}, \
            "sp21" : {0 : 0.0435, 1 : 0.0, 2 : 0.0, 3 : 0.5281, 4 : 0.1288, 5 : 0.2465, \
                    6 : 0.1884, 7 : 0.5223, 8 : 0.0, 9 : 0.3726, 10 : 0.1851, \
                    11 : 0.3299, 12 : 0.2256}, \
            "sp22" : {0 : 0.0376, 1 : 0.0, 2 : 0.0, 3 : 0.5673, 4 : 0.1248, 5 : 0.3204, \
                    6 : 0.2594, 7 : 0.4171, 8 : 0.0, 9 : 0.2863, 10 : 0.1843, \
                    11 : 0.3706, 12 : 0.2524}
                     }

# Categories
# 0: strawberry
# 1: angora
# 2: axolotl
# 3: sea cucumber
# 4: gown
# 5: persian cat
# 6: hoopskirt
# 7: acorn
# 8: siamese cat
# 9: bath towel
# 10: dough
# 11: coffeepot
# 12: screen

examplePet = {0 : 0.8, 1 : 0.8, 2 : 0.2, 3 : 0.1, 4 : 0.4, 5: 0.6, 6: 0.3, \
              7: 0.8, 8 : 0.4653, 9 : 0.1126, 10 : 0.4220, 11 : 0.0, 12 : 0.0}

def featureDistance(userInput):

    bestSpecies = None
    bestDistance = None

    for key in speciesDict:
        sums = 0
        species = speciesDict[key]
        for i in range(len(categories)):
            category = catNums[i]

            userFeature = userInput[category]
            speciesFeature = species[category]
            sums += (userFeature - speciesFeature)**2
        distance = math.sqrt(sums)
        if (bestDistance == None) or (distance < bestDistance):
            bestDistance = distance
            bestSpecies = key

    speciesID = (str(bestSpecies).split("sp"))[1]
    return speciesID

print(featureDistance(examplePet))