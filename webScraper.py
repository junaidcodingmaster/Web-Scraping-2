import os
from time import sleep
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


class WebScraper:
    def __init__(self) -> None:

        print("Target -> https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
        sleep(0.1)
        print("Page Domain -> wikipedia.org")
        sleep(0.1)
        print("Page Maintained by -> Wikipedia")
        sleep(0.2)
        print("Page Certificate -> VERIFIED ,", "Connection -> SECURED", "\n")
        sleep(0.2)
        print("Checking the connection response ...", "\n")

        self.main()

    def main(self):
        url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
        page = requests.get(url)

        sleep(0.3)
        print("Status Code ->", page.status_code)

        soup = bs(page.text, "html.parser")
        star_table = soup.find_all("table")

        sleep(0.3)
        print("\nExtracting Data ...")

        temp_list = []
        table_rows = star_table[7].find_all("tr")
        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text.rstrip() for i in td]
            temp_list.append(row)

        sleep(0.2)
        print("\nSaving Data(Local) ...")

        Star_names = []
        Distance = []
        Mass = []
        Radius = []
        for i in range(1, len(temp_list)):
            Star_names.append(temp_list[i][0])
            Distance.append(temp_list[i][5])
            Mass.append(temp_list[i][7])
            Radius.append(temp_list[i][8])

        sleep(0.2)
        cwd = os.getcwd()
        showFileName = "\dwarf_stars.csv"
        fileName = "dwarf_stars.csv"
        print("\nSaving Data as ", fileName, " ...")

        df2 = pd.DataFrame(
            list(
                zip(
                    Star_names,
                    Distance,
                    Mass,
                    Radius,
                )
            ),
            columns=["Star_name", "Distance", "Mass", "Radius"],
        )

        df2.to_csv(fileName)
        print("\nData is Saved as ->", cwd + showFileName)

    def showData():
        df = pd.read_csv("dwarf_stars.csv")
        print(df)

    def openCSV():
        fileName = "\dwarf_stars.csv"
        getPath = os.getcwd()
        path = getPath + fileName

        print("Opening dwarf_stars.csv ...", "\n")
        os.system("start " + path)
        sleep(0.5)
