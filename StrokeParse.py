import json

#  Remove duplicate point return by canvas element      
def removeDuplicates(strokes):
    newStrokes=[]
    for stroke in strokes:
        newstroke= []
        newXPoints = []
        newYPoints = []
        xPoints = stroke[0]
        yPoints = stroke[1]
        pointCount = len(xPoints)
        for i in range(pointCount-1):
            if(xPoints[i]==xPoints[i+1] and yPoints[i]==yPoints[i+1]):
                continue
            else:
                newXPoints.append(xPoints[i+1])
                newYPoints.append(yPoints[i+1])
        newstroke.append(newXPoints)
        newstroke.append(newYPoints)
        newStrokes.append(newstroke)
    return newStrokes    

# Parse the data return from canvas and create data structure
#    [ 
#  [  // First stroke 
#    [x0, x1, x2, x3, ...],
#    [y0, y1, y2, y3, ...],
#  ],
#  [  // Second stroke
#    [x0, x1, x2, x3, ...],
#    [y0, y1, y2, y3, ...],
#  ],
#]

def compressData(content): 
    parsed_json = json.loads(content)
    strokes = []
    strokeSize=[]
    for singleStroke in parsed_json:
        lines = singleStroke["lines"]
        strokeSize.append(singleStroke["size"])
        stroke = []
        xLine=[]
        yLine=[]
        for line in lines:
            startPoint = line['start']
            endPoint = line['end']
            xLine.append(int(startPoint['x']))
            xLine.append(int(endPoint['x']))
            yLine.append(int(startPoint['y']))
            yLine.append(int(endPoint['y']))
        stroke.append(xLine)
        stroke.append(yLine)
        strokes.append(stroke)
    
    strokes = removeDuplicates(strokes)
    return strokes     

