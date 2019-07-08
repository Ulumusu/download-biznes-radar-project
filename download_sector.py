import pandas as pd

df = pd.read_csv("Nazwy.csv")
rows = df.shape[0]
print(rows)
a = df["Skrot"]
data_list = []
data_list_name = []

for company in a:
    try:
        site = pd.read_html("https://www.biznesradar.pl/notowania/" + str(company) + "#1d_lin_lin")
        data = len(site)
        for x in range(data):
            frame = site[x]
            rows = frame.shape[0]
            for row in range(rows):
                if frame.iloc[row, 0] == "Sektor:":
                    string_name = str(frame.iloc[row, 1])
                    data_list_name.append(str(company))
                    data_list.append(string_name)
                    print(str(company) + " " + string_name)
    except:
        data_list_name.append(str(company))
        data_list.append("Nie ma")
        print(str(company) + " " + "Nie ma")

data_frame = pd.DataFrame({"Skrot":data_list_name, "Sektor":data_list})
data_frame.to_csv("sektor.csv")
data_frame.to_excel("sektor.xlsx")


