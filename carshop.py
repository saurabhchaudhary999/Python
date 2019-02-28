import operator

def car():
    print("**************")
    print("Enter numbers of cars need for rent: ")
    carno = int(input())
    carrecord={}
    for car in range(0,carno ):
        print("Enter car type:")
        type= input()
        print("Enter no of days for rent:")
        rentdays= int(input())
        carrecord[type]=rentdays
    return carrecord


def driverrank(carrecord):
    try:
        print("**************")
        sortedcarrecord= sorted(carrecord.items(), key=operator.itemgetter(1), reverse =True)
        print(sortedcarrecord)
        print("{} secured rank one with {}days".format(sortedcarrecord[0][0], sortedcarrecord[0][1]))
        print("{} secured rank two with {}days".format(sortedcarrecord[1][0], sortedcarrecord[1][1]))
        print("{} secured rank three with {}days".format(sortedcarrecord[2][0], sortedcarrecord[2][1]))
        return sortedcarrecord
    except IndexError:
        print("choose min three cars")
        quit()

def bonus(sortedcarrecord, petrol):
    print("**************")
    print("{} has win {} ltr petrol".format(sortedcarrecord[0][0], petrol[0]))
    print("{} has win {} ltr petrol".format(sortedcarrecord[1][0], petrol[1]))
    print("{} has win {} ltr petrol".format(sortedcarrecord[2][0], petrol[2]))
    print("**************")

carrecord= car()
sortedcarrecord= driverrank(carrecord)
petrol = (100, 50, 30)
bonus(sortedcarrecord, petrol)
