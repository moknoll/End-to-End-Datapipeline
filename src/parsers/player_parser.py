import pandas as pd
from bs4 import BeautifulSoup
from src.parsers.base_parser import Parser

class PlayerParser(Parser): 
    def parse(self, soup: BeautifulSoup) -> pd.DataFrame: 
        """Get all reqired HTML elements once"""
        elements = soup.find_all("img", class_="bilderrahmen-fixed lazy lazy")
        stats = soup.find_all("td", class_="zentriert")
        positions = soup.find_all("td", class_="posrela")

        # Split repeating player stats
        numbers = stats[0::8]
        ages = stats[1::8]
        countries = stats[2::8]
        heights = stats[3::8]
        feet = stats[4::8]
        # joined_club = stats[5::8]
        transfers = stats[6::8]
        contract = stats[7::8]

        players = []

        for index, element in enumerate(elements): 
            player = {
                "name": element.get("title"),
                "number": self._parse_number(numbers[index]),
                "dob": self._parse_dob(ages[index]), 
                "age": self._parse_age(ages[index]), 
                "country": self._parse_country(countries[index]), 
                "height": heights[index].text.strip()
                    if heights[index].text else None,
                "foot": feet[index].text.strip()
                    if feet[index].text else None,
                "contract": contract[index].text.strip()
                    if contract[index].text else None, 
                "signed_from": self._parse_signed_from(transfers[index]),
                "signing_fee": self._parse_fee(transfers[index]),
                "position": self._parse_position(positions[index])
            }

            players.append(player)
        return pd.DataFrame(players)
    
    def _parse_number(self, element): 
        number = element.find("div", class_="rn_nummer")
        return number.text.strip() if number else None

    def _parse_age(self, element):
        if not element.text:
            return None
        return element.text.split("(")[1].split(")")[0]
    
    def _parse_dob(self, element): 
        if not element.text: 
            return None
        return element.text.split("(")[0].strip()
    
    def _parse_country(self, element): 
        img = element.find("img")
        return img.get("title") if img else None
    
    def _parse_signed_from(self, element):
        link = element.find("a")
        if not link: 
            return None
        return link.get("title").split(":")[0]
    
    def _parse_fee(self, element):
        link = element.find("a")
        if not link: 
            return None
        title = link.get("title")
        if "Ablöse" not in title: 
            return None 
        return title.split("Ablöse ")[1]
    
    def _parse_position(self, element): 
        rows = element.find_all("tr")

        if len(rows) > 1: 
            return rows[1].find("td").text.strip()
        return None                              
