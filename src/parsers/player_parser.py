import pandas as pd
from bs4 import BeautifulSoup

from .parser import Parser

class PlayerParser(Parser): 
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame: 
        elements = soup.find_all("img", _class= "bilderrahmen-fixed lazy lazy")
        names = [td.get("title") if td.get("title") else None for td in elements]
        return pd.DataFrame(names, columns=["name"])
    