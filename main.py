import art
import clear
import gameData
import random

def selectNextIndexes(dataList, indexes):
    first = indexes[0]
    next = indexes[1]

    first = next

    if next + 1 <= len(dataList):
        next += 1

    indexes[0] = first
    indexes[1] = next

    return indexes

def dataSelected(data, indexes):
    first = indexes[0]
    next = indexes[1]

    dataList = [data[first], data[next]]

    return dataList

def compareFollowers(firstFollowers, secondFollowers):
    if firstFollowers > secondFollowers:
        return 1
    elif firstFollowers < secondFollowers:
        return 2
    else: 
        return 0

DATA_SIZE = len(gameData.data)
logo = art.logo
vs = art.vs
first = 0
next = 1
indexes = [first, next]
data = random.sample(gameData.data, DATA_SIZE)
again = True
score = 0
print(logo)

while again:
    indexes = selectNextIndexes(data, indexes)
    dataList = dataSelected(data, indexes)

    firstComp = dataList[0]
    secondComp = dataList[1]
    followersSelected = 0
    followersToCompare = 0

    firstName = firstComp["name"]
    firstFollowerCount = firstComp["follower_count"]
    firstDescription = firstComp["description"]
    firstCountry = firstComp["country"]

    secondName = secondComp["name"]
    secondFollowerCount = secondComp["follower_count"]
    secondDescription = secondComp["description"]
    secondCountry = secondComp["country"]

    print(f"Compare A: {firstName}, a {firstDescription}, from {firstCountry}, followers {firstFollowerCount}")
    print(vs)
    print(f"Against B: {secondName}, a {secondDescription}, from {secondCountry}, followers {secondFollowerCount}")
    
    choise = input("Who has more followers? Type 'A' or 'B': ").lower()

    if choise == "a":
        followersSelected = firstFollowerCount
        followersToCompare = secondFollowerCount
    else:
        followersSelected = secondFollowerCount
        followersToCompare = firstFollowerCount
    
    comparisonWinner = compareFollowers(followersSelected, followersToCompare)

    if comparisonWinner == 1:
        score += 1
        again = True
    elif comparisonWinner == 2:
        again = False
    else:
        score = -1
        again = False

    clear.clear()
    print(logo)

    if again:
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
