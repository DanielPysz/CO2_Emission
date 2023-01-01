import csv
import pandas as pd
import numpy as np

def open_CO2(file_path):
    co2 = pd.read_csv(file_path)
    index = np.arange(1,17234, dtype=int)
    years = np.arange(1751,2015, dtype=int)
    a = co2['Year'] == 2014
    b = co2[a]
    #print(b.sort_values(by=['Per Capita'], ascending=False))

def open_GDP(file_path):
    gdp = pd.read_csv(file_path)
    gdpnow = gdp['2021'] > 0
    gdp2021 = gdp[gdpnow]
    #print(gdp)
    return gdp2021
def open_pop(file_path):
    pop = pd.read_csv(file_path)
    popnow = pop['2021'] > 0
    pop2021 = pop[popnow]
    return pop2021


open_CO2("C:/Users/danpy/OneDrive/Pulpit/co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv")
open_GDP("C:/Users/danpy/OneDrive/Pulpit/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv")
#open_pop("C:/Users/danpy/OneDrive/Pulpit/API_SP.POP.TOTL_DS2_en_csv_v2_4751604/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv")
