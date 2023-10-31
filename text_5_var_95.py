from bs4 import BeautifulSoup
import csv

items = list()

with open('text_5_var_95', encoding="utf-8") as f:
    lines = f.readlines()
    html = ''
    for line in lines:
        html += line

    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())
    rows = soup.find_all('tr')
    #print(rows)
    rows = rows[1:]
    for row in rows:
        cells = row.find_all("td")
        item = {
            'Company': cells[0].text,
            'Contact': cells[1].text,
            'Country': cells[2].text,
            'Price': cells[3].text,
            'Item': cells[4].text
        }
        items.append(item)
        #print(item)

with open('r_text_5_var_95.csv', 'w', encoding = "utf-8", newline='') as res:
    writer = csv.writer(res, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for item in items:
        writer.writerow(item.values())