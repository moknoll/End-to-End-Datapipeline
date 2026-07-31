import requests
from bs4 import BeautifulSoup
import pandas as pd
from dataclasses import dataclass

@dataclass
class Team: 
    id: str
    name: str


def scrape():
    header = {"user-agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:152.0) Gecko/20100101 Firefox/152.0"}
    team_url = "https://www.transfermarkt.de/bundesliga/startseite/wettbewerb/L1/plus/?saison_id=2026"

    team_response = requests.get(team_url, headers=header)
    team_html_code = team_response.content
    soup = BeautifulSoup(team_html_code, "html.parser")

    team_info = soup.find_all("td", class_="hauptlink no-border-links")

    teams = []
    team_id = []
    for team in team_info:
        teams.append(team.find("a").get("href").split("/")[1])
        team_id.append(team.find("a").get("href").split("/")[4])
#     market_value = soup.find_all("td", class_="rechts hauptlink")
#     elements = soup.find_all("img", class_="bilderrahmen-fixed")
#     stats = soup.find_all("td", class_="zentriert")
#     player_position = soup.find_all("td", class_="posrela")

#     num_elements = [stat for stat in stats[0::8]]    
#     age_elements = [stat for stat in stats[1::8]]
#     countries_elements = [stat for stat in stats[2::8]]
#     heights = [stat for stat in stats[3::8]]
#     foot = [stat for stat in stats[4::8]]
#     club_joined = [stat for stat in stats[5::8]]
#     club_before = [stat for stat in stats[6::8]]
#     contract = [stat for stat in stats[7::8]]

#     heights_arr = []
#     foot_arr = []
#     club_before_arr = []
#     club_joined_arr = []
#     contracts = []
#     signing_fee = []
#     countries = []
#     rn_nummer = []
#     players = []
#     dobs = []
#     ages = []
#     market_values = []
#     player_pos = []

#     for cell in countries_elements:
#         nations = [img["title"] for img in cell.find_all("img")]
#         countries.append(nations)
#     for c in contract:
#         contracts.append(c.text)
    
#     for element in club_before:
#         club_before_arr.append(element.find("a").get("title").split(":")[0])
#         signing_fee.append(element.find("a").get("title").split(":")[1].split("Ablöse ")[1])

#     for element in club_joined: 
#         club_joined_arr.append(element.text)

#     for element in heights: 
#         heights_arr.append(element.text)

#     for element in foot: 
#         foot_arr.append(element.text)
        
#     for player in player_position:
#         player_pos.append(player.find_all("tr")[1].find("td").text.strip())
        
#     for value in market_value: 
#         if value.text:
#             market_values.append(value.find("a").text)
#         else: 
#             market_values.append(None)

#     for age in age_elements: 
#         if age.text: 
#             ages.append(age.text.split(" (")[1].split(")")[0])
#         else: 
#             ages.append(None)

#     for dob in age_elements:
#         if dob.text: 
#             dobs.append(dob.text.split(" (")[0])
#         else: 
#             dobs.append(None)

#     for element in num_elements: 
#         if element.find("div", "rn_nummer"):
#             rn_nummer.append(element.find("div", "rn_nummer").text)
#         else:
#             rn_nummer.append(None)

#     for element in elements: 
#         if element.get("title"):
#             players.append(element.get("title"))
#         else: 
#             players.append(None)

#     data = {
#         "Name": players,
#         "Position": player_pos,
#         "Number":rn_nummer,
#         "Dob": dobs,
#         "Age": ages,
#         "County": countries,
#         "Height": heights_arr,
#         "Foot": foot_arr,
#         "Contract": contracts,
#         "Club_joined": club_joined_arr,
#         "Before": club_before_arr,
#         "Signing_fee": signing_fee,
#         "Market_value": market_values,
#     }
#     data = pd.DataFrame(data)
#     # print(data.head())

if __name__=='__main__':
     scrape()
