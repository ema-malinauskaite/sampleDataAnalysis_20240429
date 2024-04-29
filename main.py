print('-----------------uzdavinys is sampleData.csv failo--------------------')
from csv import reader
# uždaviniams spręsti kurkite savo funkcijas, pasidarykite taip, kad būtų patogu dirbti. k - income, d - outcome
# 1. kokios valiutos buvo naudotos?
# 2. kiek income, outcome?(ignoruojant valiutas)
# 3. kiek income, outcome pagal kiekvieną valiutą?
# 4. kiek buvo išleista kiekvieną mėnesį?
# 5. kiek buvo uždirbta kiekvieną mėnesį?
# 6. koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00)(ignoruojant valiutas)
# 7. koks pinigų likutis kiekvieno mėnesio gale? (sausio pradžioje likutis buvo 0.00) pagal kiekvieną valiutą?
# 8. atvaizduokite per procentinę išraišką pamėnesiui pajamas ir išlaidas procentine išraiška: (žemiau pvz)

with open('sampleData_results.csv', 'w') as file:
    file.write('')

with open('sampleData.csv') as file:
    csvReader = reader(file, delimiter=',')
    next(csvReader)
    data = list(csvReader)

#--------------------------

# Naudotu valiutu isvedimas i atskira masyva, sumos be valiutu
with open('sampleData.csv') as failas:
    csv_reader = reader(failas, delimiter=',')
    next(csv_reader)
    naudotosValiutos = []
    sumosBeValiutos = {}
    sumosBeValiutos['incomeSuma'] = 0
    sumosBeValiutos['outcomeSuma'] = 0
    for eilute in csv_reader:
        naudotosValiutos.append(eilute[6])
        if eilute[7] == 'K':
             sumosBeValiutos['incomeSuma'] += float(eilute[5])
        if eilute[7] == 'D':
             sumosBeValiutos['outcomeSuma'] += float(eilute[5])
    naudotosValiutos = set(naudotosValiutos)

# sumu pagal valiutas skaiciavimas
sumosIncomeValiutom = {}
sumosOutcomeValiutom = {}
for valiuta in naudotosValiutos:
    sumosIncomeValiutom[valiuta] = 0
    sumosOutcomeValiutom[valiuta] = 0
    with open('sampleData.csv') as failas:
        csv_reader = reader(failas, delimiter=',')
        next(csv_reader)
        for eilute in csv_reader:
            if eilute[7] == 'K' and eilute[6] == valiuta:
                sumosIncomeValiutom[valiuta] += float(eilute[5])
            if eilute[7] == 'D' and eilute[6] == valiuta:
                sumosOutcomeValiutom[valiuta] += float(eilute[5])

# menesiu masyvo sukurimas
with open('sampleData.csv') as failas:
    csv_reader = reader(failas, delimiter=',')
    next(csv_reader)
    menesiai = []
    menesiuISlaidos = {}
    for eilute in csv_reader:
        menesiai.append(eilute[2][5:7])
    menesiai = set(menesiai)

menesiai = sorted(list(menesiai))

#sumavimas pagal menesius
sumosIncomeMenesiais = {}
sumosOutcomeMenesiais = {}
for menesis in menesiai:
    sumosIncomeMenesiais[menesis] = 0
    sumosOutcomeMenesiais[menesis] = 0
    with open('sampleData.csv') as failas:
        csv_reader = reader(failas, delimiter=',')
        next(csv_reader)
        for eilute in csv_reader:
            if eilute[7] == 'K' and eilute[2][5:7] == menesis:
                sumosIncomeMenesiais[menesis] += float(eilute[5])
            if eilute[7] == 'D' and eilute[2][5:7] == menesis:
                sumosOutcomeMenesiais[menesis] += float(eilute[5])


print(f'Naudotos valiutos: {naudotosValiutos}') # 1 uzduotis
print(f'Sumos (be valiutos): {sumosBeValiutos}') # 2 uzd
print(f'Income pagal valiutas: {sumosIncomeValiutom}') # 3 uzd
print(f'Outcome pagal valiutas: {sumosOutcomeValiutom}') # 3 uzd
print(f'Income pagal menesius: {sumosIncomeMenesiais}') # 4 uzd
print(f'Outcome pagal menesius: {sumosOutcomeMenesiais}') # 4 uzd
print('')

# Likucio menesio gale skaiciavimas:
for valiuta in naudotosValiutos:
    suma = 0
    for menesis in menesiai:
        with open('sampleData.csv') as failas:
            csv_reader = reader(failas, delimiter=',')
            next(csv_reader)
            for eilute in csv_reader:
                if eilute[7] == 'K' and eilute[2][5:7] == menesis and eilute[6] == valiuta:
                    suma += float(eilute[5])
                if eilute[7] == 'D' and eilute[2][5:7] == menesis and eilute[6] == valiuta:
                    suma -= float(eilute[5])
            print(f'Likutis menesio {menesis} gale pagal valiuta {valiuta} yra: {suma}')
print('')

#pamenesiui procentine israiska
#-- sausis:
#-- -- income:
#-- -- Eur: 29%
#-- -- DK: 0%
#-- -- outcome:
#-- -- Eur: 36%
#-- -- DK: 19%

for menesis in menesiai:
    print('------------------------')
    print(f'menesis - {menesis}:')

    for xcome in ['K', 'D']:
        print(f'    {xcome}: ')
        for valiuta in naudotosValiutos:
            print(f'        {valiuta}: ', end='')
            suma = 0
            with open('sampleData.csv') as failas:
                csv_reader = reader(failas, delimiter=',')
                next(csv_reader)
                for eilute in csv_reader:
                    if eilute[7] == xcome and eilute[2][5:7] == menesis and eilute[6] == valiuta:
                        suma += float(eilute[5])
            if xcome == 'K' and sumosIncomeValiutom[valiuta] != 0:
                proc = round((suma/sumosIncomeValiutom[valiuta])*100, ndigits=1)
                print(f'{proc}%')
            if xcome == 'K' and sumosIncomeValiutom[valiuta] == 0:
                proc = 0.00
                print(f'{proc}%')
            if xcome == 'D' and sumosOutcomeValiutom[valiuta] != 0:
                proc = round((suma/sumosOutcomeValiutom[valiuta])*100, ndigits=1)
                print(f'{proc}%')
            if xcome == 'D' and sumosOutcomeValiutom[valiuta] == 0:
                proc = 0.00
                print(f'{proc}%')



