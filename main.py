from bs4 import BeautifulSoup
import json
import httpx

url = "https://www.vlr.gg/stats/?event_group_id=all&event_id=all&region=na&country=all&min_rounds=200&min_rating=1550&agent=all&map_id=all&timespan=all"

contents = httpx.get(url,timeout=30).text

soup = BeautifulSoup(contents, "html.parser")


class Player:
    def __init__(
        self,
        Player,
        Agents,
        Rnd,
        R,
        ACS,
        KD,
        KAST,
        ADR,
        KPR,
        APR,
        FKPR,
        FDPR,
        HS_percentage,
        CL_percentage,
        CL,
        KMax,
        K,
        D,
        A,
        FK,
        FD,
    ):
        self.Player = Player
        self.Agents = Agents
        self.Rnd = Rnd
        self.R = R
        self.ACS = ACS
        self.KD = KD
        self.KAST = KAST
        self.ADR = ADR
        self.KPR = KPR
        self.APR = APR
        self.FKPR = FKPR
        self.FDPR = FDPR
        self.HS_percentage = HS_percentage
        self.CL_percentage = CL_percentage
        self.CL = CL
        self.KMax = KMax
        self.K = K
        self.D = D
        self.A = A
        self.FK = FK
        self.FD = FD


list_of_players = []

rows = soup.find_all("tr")
for row in rows:
    cols = row.find_all("td")

    cols_text = [col.text.strip() for col in cols]
    if len(cols_text) == 0:
        continue

    img_tags = row.find_all("img")
    img_list = []
    for img in img_tags:
        img_file_name = img["src"]
        img_file_name = img_file_name.split("/")[-1][:-4]
        img_list.append(img_file_name)
    cols_text[1] = img_list
    list_of_players.append(Player(*cols_text))

with open("reuslt.json", "w", encoding="utf-8") as f:
    json.dump(
        [player.__dict__ for player in list_of_players], f, ensure_ascii=False, indent=4
    )
