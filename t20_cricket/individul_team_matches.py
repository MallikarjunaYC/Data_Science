from bs4 import BeautifulSoup
import requests
import pandas as pd

URL = "https://www.espncricinfo.com/records/tournament/team-match-results/icc-men-s-t20-world-cup-2022-23-14450"

header = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36', 'Accept-Language' : 'eng-US'
            })


webpage = requests.get(URL, headers=header)

# print(webpage.content)

soup = BeautifulSoup(webpage.content, 'html.parser')

#tables = soup.find('table', attrs={'class':'ds-w-full ds-table ds-table-xs ds-table-auto  ds-w-full ds-overflow-scroll ds-scrollbar-hide'})
tables = soup.find_all('table')
# for table in tables:
#     rows = table.find_all('tr')
#     for row in rows:
#         cells = row.find_all(['th', 'td'])  # Extract both headers and data cells
#         for cell in cells:
#             print(cell.text)  # Print the content of each cell
#         print('---')  # Separate rows with '---'

# Create an empty list to store table data
table_data = []

    # Iterate through tables
for table in tables:
    rows = table.find_all('tr')
    table_rows = []  # List to store rows of the current table

    for row in rows:
        cells = row.find_all(['th', 'td'])
        row_data = [cell.text.strip() for cell in cells]
        table_rows.append(row_data)

    # Append the table data to the list
    table_data.append(table_rows)



# Convert the list of tables into Pandas DataFrames
dataframes = [pd.DataFrame(table) for table in table_data]

#print(dataframes)

# Now you have a list of DataFrames, one for each table

df = pd.concat(dataframes, ignore_index=True)

print(df.iloc[0,6])

