import pytest
import pandas as pd
import numpy as np
import load
import calculations
import argparse

lata = load.lat(2004, 2008, pd.DataFrame(), pd.DataFrame(), pd.DataFrame())


class Test:
    def test1(self):
        assert len(lata) == 4
    def test2(self):
        lst1 = pd.DataFrame({"Country Name":["Poland", "Deutschland", "USA", "Russia", "France"]})
        lst2 = pd.DataFrame({"Country Name":["Deutschland", "Czech Republic", "France", "Maroko"]})
        lst3 = pd.DataFrame({"Year":[2001, 2001, 2002, 2002], "Country":[ "POLAND", "USA","FRANCE","DEUTSCHLAND"]})
        wsp_kraje = calculations.wspolne_kraje(lst1, lst2, lst3)
        assert wsp_kraje == ["FRANCE", "DEUTSCHLAND"]
    def test3(self):
        lata = np.arange(2003, 2007)
        lst1 = pd.DataFrame({"Year":[2001, 2002, 2003, 2004, 2005, 2006]})
        lst2 = pd.DataFrame({"Country":["A", "B","C","D"],2000:["A", "B","C","D"],  2001:["A", "B","C","D"], 2002:["A", "B","C","D"],2004:["A", "B","C","D"], 2005:["A", "B","C","D"], 2006:["A", "B","C","D"], 2007:["A", "B", "C", "D"]})
        lst3 = pd.DataFrame({"Country":["A", "B","C","D"], 1998:["A", "B","C","D"], 1999:["A", "B","C","D"], 2003:["A", "B","C","D"], 2004:["A", "B","C","D"], 2005:["A", "B","C","D"], 2006:["A", "B","C","D"], 2007:["A", "B", "C", "D"]})
        wsp_lata = calculations.wspolne_lata(lst2, lst3, lst1, lata)
        assert set(wsp_lata) == set([2004, 2005])

