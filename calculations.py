import pandas as pd
import load
import numpy as np
import argparse

def wspolne_kraje(pop, gdp, co2):
    popC = np.array(pop["Country Name"])
    gdpC = np.array(gdp["Country Name"])
    co2C = np.array(co2[co2["Year"]==int(co2["Year"][-1:])]["Country"]) #wybieramy kraje, które obecne są w ostatnim roku raportu
    popCgdpC = np.array([i for i in popC if i in gdpC])
    wsp_kraje = [i for i in co2C if i in [country.upper() for country in popCgdpC]]
    return wsp_kraje

def wspolne_lata(pop, gdp, co2, lata):
    co2_lata = np.arange(int(co2["Year"][0]), int(co2["Year"][-1:]))
    pop_lata = np.arange(int(pop.columns[4]), int(pop.columns[-2:][0]))
    gdp_lata = np.arange(int(gdp.columns[4]), int(gdp.columns[-2:][0]))
    popgdp_lata = [i for i in pop_lata if i in gdp_lata]
    wsp_lata_beta = [i for i in co2_lata if i in popgdp_lata]
    wsp_lata = [i for i in wsp_lata_beta if i in lata]
    return wsp_lata

def gdp_per_capita(pop, gdp, co2, lata):
    wsp_kraje = wspolne_kraje(pop, gdp, co2)
    wsp_lata = wspolne_lata(pop, gdp, co2, lata)
    for year in wsp_lata:
        print("Tabela GDP na osobę w roku: ", year)
        popYear = pop.sort_values(by=str(year), ascending=False)
        gdpYear = gdp.sort_values(by=str(year), ascending=False)
        country = popYear.loc[:, ["Country Name", str(year)]]
        for row in country.iterrows():
            if row[1][0] not in [i.capitalize() for i in wsp_kraje]:
                country = country.drop(index=(row[0]))
        country["gdp"] = gdpYear[str(year)]
        country = country.rename(columns={str(year): "population"})
        country["gdp/pop"] = np.divide(np.array(country[["gdp"]]), np.array(country[["population"]]))
        country = country.sort_values(by="gdp/pop", ascending=False)
        print(country.head(5))

def co2_per_capita(co2, pop, gdp, lata):
    wsp_lata = wspolne_lata(pop, gdp, co2, lata)
    co2 = co2.drop(labels=["Bunker fuels (Not in Total)", "Cement", "Gas Fuel", "Solid Fuel", "Liquid Fuel", "Gas Flaring"],axis=1)
    for year in wsp_lata:
        co = co2["Year"] == year
        co2Year = co2[co].sort_values(by="Per Capita", ascending=False)
        print("Emisja CO2 per capita dla roku:", year)
        print(co2Year.head(5))

def wzrost_emisji(co2, gdp, pop, lata):
    wsp_kraje = wspolne_kraje(pop, gdp, co2)
    wsp_lata = wspolne_lata(pop, gdp, co2, lata)
    co2 = co2.drop(labels=["Bunker fuels (Not in Total)", "Cement", "Gas Fuel", "Solid Fuel", "Liquid Fuel", "Gas Flaring"],axis=1)
    now = co2["Year"] == wsp_lata[-1]
    past = co2["Year"] == wsp_lata[0]
    now = co2[now].sort_values(by="Country")
    past = co2[past].sort_values(by="Country")
    contr_beta = [i for i in np.array(now["Country"]) if i in np.array(past["Country"])]
    contr = [i for i in contr_beta if i in wsp_kraje]
    for row in now.iterrows():
        if row[1][1] not in contr :
            now = now.drop(index=(row[0]))
    for row in past.iterrows():
        if row[1][1] not in contr:
            past = past.drop(index=(row[0]))
    now["Zmiana"] = np.subtract(np.array(now[["Per Capita"]]), np.array(past[["Per Capita"]]))
    print("Zmiana emisji CO2:")
    print(now.sort_values(by="Zmiana", ascending=False))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analiza danych")
    parser.add_argument("-c","--path_co2", required=False, type=str, help="Path to co2 emission file")
    parser.add_argument("-p","--path_pop",required=False, type = str, help="Path to population file")
    parser.add_argument("-g","--path_gdp",required=False, type=str, help = "Path to gdp file")
    parser.add_argument("-s","--start",required=False, type=int, help="Year when the calculations starts")
    parser.add_argument("-k","--koniec",required=False, type=int, help="Year when the calculations stops")
    args = parser.parse_args()
    co2 = load.open_CO2(args.path_co2)
    pop = load.open_pop(args.path_pop)
    gdp = load.open_GDP(args.path_gdp)
    lata = load.lat(args.start, args.koniec, co2, pop, gdp)

#Komentarz
