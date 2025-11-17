Projekt_3 Elections Scraper

This project is a web scraper designed to extract results from the Czech parliamentary elections (2017). The script downloads official data directly from the website volby.cz and exports the collected results into a structured .csv file.



This repository contains exactly the required files:

main.py

requirements.txt

README.md 

strakonice.csv – example CSV file containing scraped election data

HOW TO INSTALL

1. Create a virtual environment and activate it
2. Install required libraries (listed in requirements.txt)
    $ pip install requests
    $ pip install
    $ pip install beautifulsoup4
   
HOW TO USE
The program requires two arguments:
  1. URL link – from field X
  2. Filename – name of the resulting file (without .csv)
Run the craper
  python main.py "URL" "filename"

EXAMPLE RUN
python main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3106" "strakonice"
Starting data download...
Saving to file...
Done – output saved as strakonice.csv
