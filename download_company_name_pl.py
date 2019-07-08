from bs4 import BeautifulSoup
import requests
import pandas as pd


def download_name_poland():
    global dt_company_name
    dt_company_name = pd.DataFrame(columns=["Skrot", "Nazwa", "Druga"])
    url_list = ["https://www.biznesradar.pl/gielda/akcje_gpw", "https://www.biznesradar.pl/gielda/newconnect"]
    for url in url_list:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        label = soup.find("table", {"class": "qTableFull"}).find_all("a", {'class': "s_tt"})
        for x in label:
            string_link = str(x)
            find = string_link.find("/notowania/")
            del_not_important = string_link[(find + 11):]

            link_name_number = del_not_important.find(" ")
            link_name = del_not_important[:link_name_number - 1]  # link address

            title_name_number = del_not_important.find("title=")
            end_title_name_number = del_not_important.find(">")
            title_name = del_not_important[(title_name_number + 7): (end_title_name_number - 1)]

            end_second_name_number = del_not_important.find("<")
            second_name = del_not_important[(end_title_name_number + 1): (end_second_name_number)]

            dt_company_name = dt_company_name.append({
                "Skrot": link_name,
                "Nazwa": title_name,
                "Druga": second_name},
                ignore_index=True)

download_name_poland()
dt_company_name.to_csv("Nazwy.csv")
dt_company_name.to_excel("Nazwy.xlsx")