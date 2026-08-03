from .base_parser import Parser
import pandas as pd

class MarketValueParser(Parser): 
    def parse(self, soup) -> pd.DataFrame:
       elements = soup.find_all("td", class_="rechts hauptlink")
       market_values  = []
       for element in elements:
            if element.find("a"): 
               market_values.append(element.find("a").text)
            else: 
               market_values.append(None)
       return pd.DataFrame({"market_value": market_values})