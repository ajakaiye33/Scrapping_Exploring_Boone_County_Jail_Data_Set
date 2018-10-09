
import sys
print(sys.executable)
print(sys.version)
import csv
import requests
from bs4 import BeautifulSoup


url = "https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody', attrs={'class': 'stripe'})

list_of_row = []
for row in table.findAll('tr')[1:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp:', '')
        list_of_cells.append(text)
    list_of_row.append(list_of_cells)

outfile = open("./inmates.csv", "w")
writer = csv.writer(outfile)
writer.writerow(['Last', 'First', 'Middle', 'Gender', 'Race', 'Age', 'City', 'State'])
writer.writerows(list_of_row)
