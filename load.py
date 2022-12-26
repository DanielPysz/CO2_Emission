import csv

def open_CO2(file_path):
    lst = []
    dzCO2 = {}
    with open(file_path, "r") as co2:
        csread = csv.reader(co2, delimiter = ",")
        table = list(csread)
        a = table[1:][17231][1]
        for i in range(len(table)-2):
            if table[1:][i][1] in lst:
                pass
            else:
                lst.append(table[1:][i][1])
        for country in lst:
            ems = {}
            for y in range(len(table)-2):
                if table[1:][y][1] == lst[lst.index(country)]:
                    ems[table[1:][y][0]] = table[1:][y][2]
                else:
                    pass
            dzCO2[country] = ems

    print(dzCO2)
open_CO2("C:/Users/danpy/OneDrive/Pulpit/co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv")


