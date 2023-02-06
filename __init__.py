import argparse
import load
import calculations

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analiza danych")
    parser.add_argument("-c", "--path_co2", required=False, type=str, help="Path to co2 emission file")
    parser.add_argument("-p", "--path_pop", required=False, type=str, help="Path to population file")
    parser.add_argument("-g", "--path_gdp", required=False, type=str, help="Path to gdp file")
    parser.add_argument("-s", "--start", required=False, type=int, help="Year when the calculations starts")
    parser.add_argument("-k", "--koniec", required=False, type=int, help="Year when the calculations stops")
    args = parser.parse_args()
    co2 = load.open_CO2(args.path_co2)
    pop = load.open_pop(args.path_pop)
    gdp = load.open_GDP(args.path_gdp)
    lata = load.lat(args.start, args.koniec, co2, pop, gdp)
    gdp_per_cap = calculations.gdp_per_capita(pop, gdp, co2, lata)
    co2_per_cap = calculations.co2_per_capita(co2, pop, gdp, lata)
    wzr_emisji = calculations.wzrost_emisji(co2, gdp, pop, lata)
