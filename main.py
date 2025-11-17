import sys
import bs4
import requests
import csv

def download(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    return soup

def get_links(soup):
    links = []
    for link in soup.select("td.cislo a"):
        links.append("https://volby.cz/pls/ps2017nss/" + link["href"])
    return links

def get_codes(soup):
    codes = []
    for code in soup.select("td.cislo a"):
        codes.append(code.get_text())
    return codes

def get_party_names(soup):
    names = []
    cells = soup.find_all("td", "cislo")
    for cell in cells:
        names.append(cell.find_next_sibling("td").get_text())
    return names

def get_vote_counts(soup, column_index):
    votes = []
    for cell in soup.select(f"div.t2_470 table tr td:nth-of-type({column_index})"):
        votes.append(cell.get_text())
    return votes

def scrape_results(links):
    print("Starting data download...")
    header = ["Číslo obce", "Název obce", "Voliči v seznamu", "Vydané obálky", "Platné hlasy"]
    results = []
    index = 0
    for municipality in links:
        row = []
        soup_main = download(source_url)
        names = get_party_names(soup_main)
        codes = get_codes(soup_main)
        row.append(codes[index])
        row.append(names[index])
        index += 1
        soup_detail = download(municipality)
        for i, element in enumerate(soup_detail.find_all("td", class_="cislo")):
            if i in (3, 4, 7):
                row.append(str(element.get_text()).replace(u'\xa0', u' '))
            elif i == 8:
                break
        for vote in get_vote_counts(soup_detail, 3):
            row.append(vote)
        results.append(row)

    soup_detail = download(municipality)
    for party in get_vote_counts(soup_detail, 2):
        header.append(party + " (votes)")

    return results, header

def save_to_csv(results):
    with open(f"{filename}.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(results[1])
        writer.writerows(results[0])

if __name__ == "__main__":
    try:
        source_url = sys.argv[1]
        filename = sys.argv[2]
        results = scrape_results(get_links(download(source_url)))
        print("Saving to file...")
        save_to_csv(results)
        print(f"Done – file saved as {filename}.csv")
    except:
        print("Error: You must provide two arguments – a URL and a filename (without .csv)")
