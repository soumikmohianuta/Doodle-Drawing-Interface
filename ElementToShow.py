from random import randint
import os

# get name of the element to show

def getElementList(directory):
    elementList = []
    for files in os.listdir(directory):
        elementList.append(files.replace('.png',''))
    return elementList

def getElementName(directory):
    elementList = getElementList(directory)
    noOfElement= len(elementList)

    randNo = (randint(0, noOfElement-1))

    return elementList[randNo]

