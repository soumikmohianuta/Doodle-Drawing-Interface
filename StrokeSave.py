import os


# create unique file Name by parsing the storing folder
def getFileName(folder, currentFile):
    maxCount = 0
    for file in os.listdir(folder):
        if currentFile in file:
            countStr = file.split('_')
            curCount = int(countStr)
            if(curCount<maxCount):
                maxCount = curCount
                
    return currentFile+"_"+str(maxCount)


# Store the stroke into the StoreElement folder
def savelocally(folder,fileName, stroke):
    fullPath = os.path.join(folder,fileName)
    file = open(fullPath, 'w+')
    file.write(str(stroke))
    file.close()
            