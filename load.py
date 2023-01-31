import pandas as pd
import numpy as np
import argparse
#if __name__ == "__main__":
parser = argparse.ArgumentParser(description="Analiza danych")
parser.add_argument("-c","--path_co2", required=False, type=str, help="Path to co2 emission file")
parser.add_argument("-p","--path_pop",required=False, type = str, help="Path to population file")
parser.add_argument("-g","--path_gdp",required=False, type=str, help = "Path to gdp file")
parser.add_argument("-s","--start",required=False, type=int, help="Year when the calculations starts")
parser.add_argument("-k","--koniec",required=False, type=int, help="Year when the calculations stops")
args = parser.parse_args()
def open_CO2(path_co2):
    co2 = pd.read_csv(path_co2)
    return co2
def open_GDP(path_gdp):
    gdp = pd.read_csv(path_gdp)
    return gdp
def open_pop(path_pop):
    pop = pd.read_csv(path_pop)
    return pop

def lat(start, koniec):
    lata = np.arange(start, koniec)
    return lata
open_CO2(args.path_co2)
lat(args.start, args.koniec)
#open_GDP(args.gdp)
#open_pop(args.pop)
#pop = C:/Users/danpy/OneDrive/Pulpit/API_SP.POP.TOTL_DS2_en_csv_v2_4751604/API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv
#gdp = C:/Users/danpy/OneDrive/Pulpit/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv
#co2 = "C:/Users/danpy/OneDrive/Pulpit/co2-fossil-by-nation_zip/data/fossil-fuel-co2-emissions-by-nation_csv.csv"
