import pandas as pd
import numpy as np
import argparse


def open_CO2(path_co2):
    co2 = pd.read_csv(path_co2)
    return co2
def open_GDP(path_gdp):
    gdp = pd.read_csv(path_gdp)
    return gdp
def open_pop(path_pop):
    pop = pd.read_csv(path_pop)
    return pop

def lat(start, koniec, co2, pop, gdp):
    if start and koniec > 0:
        lata = np.arange(start, koniec)
        return lata
    else:
        co2_lata = np.arange(int(co2["Year"][0]), int(co2["Year"][-1:]))
        pop_lata = np.arange(int(pop.columns[4]), int(pop.columns[-2:][0]))
        gdp_lata = np.arange(int(gdp.columns[4]), int(gdp.columns[-2:][0]))
        popgdp_lata = [i for i in pop_lata if i in gdp_lata]
        lata = [i for i in co2_lata if i in popgdp_lata]
        return lata

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analiza danych")
    parser.add_argument("-c", "--path_co2", required=False, type=str, help="Path to co2 emission file")
    parser.add_argument("-p", "--path_pop", required=False, type=str, help="Path to population file")
    parser.add_argument("-g", "--path_gdp", required=False, type=str, help="Path to gdp file")
    parser.add_argument("-s", "--start", required=False, type=int, help="Year when the calculations starts")
    parser.add_argument("-k", "--koniec", required=False, type=int, help="Year when the calculations stops")
    args = parser.parse_args()
    open_CO2(args.path_co2)
    lat(args.start, args.koniec)
