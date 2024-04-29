import csv

def getListFromCSV(file):
    with open(file) as file:
        csvReader = csv.DictReader(file, delimiter=',')
        sampleData = list(csvReader)
    return sampleData

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