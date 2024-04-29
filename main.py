import functions
import yaml

sampleData = functions.getListFromCSV('sampleData.csv')

currencyValues = {}
for row in sampleData:
    DK = row['D/K']
    currency = row['Valiuta']
    value = float(row['Suma'])
    currencyValues[DK] = functions.createEmpty(currencyValues, DK, {})
    currencyValues[DK][currency] = functions.createEmpty(currencyValues[DK], currency, 0.0)
    currencyValues[DK][currency] += value

currencyValues = functions.zeroInEmpty(currencyValues)
print('By currency:\n', yaml.dump(currencyValues, default_flow_style=False))

monthValues = {}
for row in sampleData:
    month = row['Data'][5:7]
    DK = row['D/K']
    value = float(row['Suma'])
    monthValues[month] = functions.createEmpty(monthValues, month, {})
    monthValues[month][DK] = functions.createEmpty(monthValues[month], DK, 0.0)
    monthValues[month][DK] += value
print('By month:\n', yaml.dump(monthValues, default_flow_style=False))

monthEndValue = {}
for row in sampleData:
    currency = row['Valiuta']
    month = row['Data'][5:7]
    value = float(row['Suma'])
    monthEndValue[currency] = functions.createEmpty(monthEndValue, currency, {})
    monthEndValue[currency][month] = functions.createEmpty(monthEndValue[currency], month, 0.0)
    if row['D/K'] == 'K':
        monthEndValue[currency][month] += value
    if row['D/K'] == 'D':
        monthEndValue[currency][month] -= value
print('Net value by the end of the month:\n', yaml.dump(monthEndValue, default_flow_style=False))

percentageValue = {}
for row in sampleData:
    month = row['Data'][5:7]
    DK = row['D/K']
    currency = row['Valiuta']
    value = float(row['Suma'])
    percentageValue[month] = functions.createEmpty(percentageValue, month, {})
    percentageValue[month][DK] = functions.createEmpty(percentageValue[month], DK, {})
    percentageValue[month][DK][currency] = functions.createEmpty(percentageValue[month][DK], currency, 0.0)
    percentageValue[month][DK][currency] += value

for month in percentageValue:
    percentageValue[month] = functions.zeroInEmpty(percentageValue[month])

for month in percentageValue:
    for DK in percentageValue[month]:
        for currency in percentageValue[month][DK]:
            if percentageValue[month][DK][currency] > 0.0:
                percentageValue[month][DK][currency] = round(percentageValue[month][DK][currency]/currencyValues[DK][currency]*100, 2)
print('Percentage:\n', yaml.dump(percentageValue, default_flow_style=False))
