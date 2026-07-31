from abc import ABC, abstractmethod 
import pandas as pd
from bs4 import BeautifulSoup

class Parser(ABC): 

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame:
        pass