import pandas as pd

names = pd.read_csv("names_and_sectors.csv")
dane = names.iloc[51:]


def clean_data(url):
    global test_df, headers
    test_df = url[0]
    rows = test_df.shape[0]
    columns = test_df.shape[1]
    for column in range(columns):
        for row in range(rows):
            string_cell = str(test_df.iloc[row, column])
            string_cell = ''.join(string_cell.split())
            end_rr = string_cell.find('r/r')
            end_kk = string_cell.find('k/k')
            end_sektor = string_cell.find("~sektor")
            if end_rr != -1:
                try:
                    test_df.iloc[row, column] = (string_cell[:end_rr])
                except ValueError:
                    test_df.iloc[row, column] = 0
            elif end_kk != -1:
                try:
                    test_df.iloc[row, column] = (string_cell[:end_kk])
                except ValueError:
                    test_df.iloc[row, column] = 0
            else:
                try:
                    test_df.iloc[row, column] = string_cell
                except:
                    continue
    if pd.isna(test_df.iloc[0, -1]) == True:
        test_df.drop(test_df.columns[[-1, ]], axis=1, inplace=True)
    test_df.iloc[0, 0] = "Data"
    test_df = test_df.T
    headers = test_df.iloc[0]
    #print(headers)

'''
url = pd.read_html("https://www.biznesradar.pl/raporty-finansowe-rachunek-zyskow-i-strat/06N,Q",
                           attrs={'class': "report-table"})


clean_data(url)
balance_df = pd.DataFrame(test_df.values[1:], columns=headers)
print(list(balance_df.columns))

print(names["Skrot"])
'''

for company in dane["Skrot"]:
    url_list = [
        "https://www.biznesradar.pl/raporty-finansowe-rachunek-zyskow-i-strat/" + str(company) + ",Q",
        "https://www.biznesradar.pl/raporty-finansowe-bilans/" + str(company) + ",Q,0",
        "https://www.biznesradar.pl/raporty-finansowe-przeplywy-pieniezne/" + str(company) + ",Q",
        "https://www.biznesradar.pl/wskazniki-wartosci-rynkowej/" + str(company),
        "https://www.biznesradar.pl/wskazniki-rentownosci/" + str(company),
        "https://www.biznesradar.pl/wskazniki-przeplywow-pienieznych/" + str(company),
        "https://www.biznesradar.pl/wskazniki-zadluzenia/" + str(company),
        "https://www.biznesradar.pl/wskazniki-plynnosci/" + str(company),
        "https://www.biznesradar.pl/wskazniki-aktywnosci/" + str(company)
    ]
    data = []
    for url in url_list:
        print(url)
        try:
            read = pd.read_html(url, attrs={'class': "report-table"})
            clean_data(read)
            d = pd.DataFrame(test_df.values[1:], columns=headers)
            #print(d.iloc[-1])
            data.append(d)
        except:
            continue
    df = pd.concat([x for x in data], axis=1, join_axes=[data[1].index])
    df.to_excel("dane/company"+ str(company)+".xlsx")
