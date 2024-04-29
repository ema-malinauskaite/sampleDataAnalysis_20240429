import csv

# Gets data as a list of dictionaries from csv file:
def getListFromCSV(file):
    with open(file) as file:
        csvReader = csv.DictReader(file, delimiter=',')
        sampleData = list(csvReader)
    return sampleData


# Adds zero values if there are non in a given level:
def zeroInEmpty(dict):
    allValues = set()
    for a in dict:
        for b in dict[a]:
            allValues.update(list(dict[a]))
    allValues = list(allValues)
    for a in dict:
        for i in allValues:
            if i not in dict[a]:
                dict[a][i] = 0.0
    return dict


# Creates empty dictionary ( if {} is given) or zero value (if 0 is given). It is usefull in FOR cycles.
def createEmpty(dict, levelName, emptyValue):
    if levelName not in dict:
        dict[levelName] = emptyValue
    return dict[levelName]
