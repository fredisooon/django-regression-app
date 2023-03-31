import json

def getPriorityList(request):
    sendedMap = request.POST['priority']
    myMapDict = json.loads(sendedMap)
    myDict = {k:v for k, v in myMapDict}
    print(myDict)
    priorityList = [-1 for i in range(len(myDict))]
    for key, value in myDict.items():
        print(priorityList)
        print(key, value)
        priorityList[int(value)] = key
    
    return priorityList