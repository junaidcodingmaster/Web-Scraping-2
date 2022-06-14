import os
import pyfiglet
from simple_chalk import chalk

from webScraper import WebScraper

# onStartUp
os.system("cls")
print("\n")

# Logo
rawLogo = pyfiglet.figlet_format("Web")
rawSideLogo = pyfiglet.figlet_format("Scraping - 2")
logo = chalk.blue.bold(rawLogo)
sideLogo = chalk.green.bold(rawSideLogo)

# output
print(logo + "\n" + sideLogo)
print("Web Scraping - 2 -> version - 2 , Made By Junaid.", "\n")
print("-" * 50)
print("Starting Web Scraping ...")
print("\n⬇⬇⬇ Logs of Web Scraping ,press 'Ctrl + C' to stop Web Scraping ⬇⬇⬇")
print("-" * 70, "\n")
# # --------------------------------------------

WebScraper()

print("\n", "-" * 50, "\n")
a = input("You want to see Web Scrapped data (y / n) -> ")
print("\n", "-" * 50, "\n")


if a == "y":
    b = input("You want to see data -> Here only[y] or in Excel[ e ] or Cancel[n] -> ")
    print("\n", "-" * 50, "\n")

    if b == "y":
        print("-" * 80, "\n")
        WebScraper.showData()
        print("\n", "-" * 80, "\n")
    elif b == "e":
        print("-" * 80, "\n")
        WebScraper.openCSV()
        print("-" * 80, "\n")
    elif b == "n":
        print(chalk.yellow("User Exited !"))
        os._exit(0)
    else:
        print(chalk.red("Incorrect Input Value !"))
        os._exit(1)

elif a == "n":
    print(chalk.yellow("User Exited !"))
    os._exit(0)
else:
    print(chalk.red("Incorrect Input Value !"))
    os._exit(1)

# # --------------------------------------------

print(
    chalk.blue.bold("Web"),
    chalk.green.bold("Scraping"),
    ", Version - 2 @ 14 June 2022 .\n",
)
print(chalk.black.bgWhite("-> Made By Junaid <-"))
