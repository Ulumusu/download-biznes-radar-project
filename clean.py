import pandas as pd

lista = ["ALIOR-BANK", "BGZ-BNP-PARIBAS", "BANK-HANDLOWY",
         "BANK-OCHRONY-SRODOWISKA", "GETIN-NOBLE-BANK",
         "GETIN-HOLDING", "IDEA-BANK", "ING-BANK-SLASKI",
         "MBANK 87", "BANK-MILLENNIUM", "PEKAO", "PKO",
         "SANTANDER", "SPL", "UNICREDIT", "MBANK"]

names = pd.read_excel("names_and_sectors.xlsx")
df = pd.read_excel("company11-BIT-STUDIOS.xlsx")
names = names[504:]
for name in names["Skrot"]:
    if name in lista:
        print("bank " + str(name))
        continue
    else:
        try:
            file = "company" + str(name) + ".xlsx"

            df = pd.read_excel(file)
            df_final = pd.DataFrame(df.iloc[:,:61])
            df_final = df_final.set_index("Data")
            df_final_two = pd.DataFrame(df.iloc[:,61:])
            df_final_two = df_final_two.set_index("Data.3")

            for x in df_final.index:
                value = 0
                if x in df_final_two.index:
                    value = 1
                if value == 0:
                    df_final = df_final.drop(x)

            for x in df_final_two.index:
                value = 0
                if x in df_final.index:
                    value = 1
                if value ==0:
                    df_final_two = df_final_two.drop(x)

            #print(str(name) + " " + str(df_final.shape[0]) + " " + str(df_final_two.shape[0]))
            df_final = df_final.reset_index()
            df_final_two = df_final_two.reset_index()
            df_final_title = pd.DataFrame(columns=["Skrot"])
            number = names.loc[names["Skrot"] == name]
            l1 = []
            l2 = []
            l3 = []
            l4 = []
            for x in range(df_final.shape[0]):
                l1.append(str(name))
                l2.append(str(number.iloc[0,1]))
                l3.append(str(number.iloc[0,2]))
                l4.append(str(number.iloc[0,3]))
            df_final_title["Skrot"] = l1
            df_final_title["Nazwa"] = l2
            df_final_title["Druga"] = l3
            df_final_title["Sektor"] = l4
            #print(df_final_title)
            mega_frame = pd.concat([df_final_title, df_final, df_final_two], axis=1, join_axes=[df_final_title.index])
            mega_frame = mega_frame.drop(columns=["Data.1", "Data.2", "Data.3", "Data.4", "Data.5", "Data.6", "Data.7", "Data.8"])


            rows = mega_frame.shape[0]
            columns = mega_frame.shape[1]
            if columns != 120:
                print(name,columns)
            for column in range(columns):
                for row in range(rows):
                    string_cell = str(mega_frame.iloc[row, column])
                    string_cell = ''.join(string_cell.split())
                    end = string_cell.find('~sektor')
                    if end != -1:
                        mega_frame.iloc[row, column] = string_cell[:end]

            #mega_frame.to_excel("kom3/" + str(name) + ".xlsx")
            mega_frame.to_csv("kom3/" + str(name) +".csv")
            print("ok " + str(name))
        except FileNotFoundError:
            continue



















'''
for x in range(row):
    cell = df.iloc[x,0]
    value = 0
    for y in range(row_two):
        cell_two = df_final_two.iloc[y,0]
        if cell == cell_two:
            print("yes")
            value += 1
    if value == 0:
        df_final = df_final.drop(df.index[x])
df_final = df.drop(columns=["Data.1","Data.2"])
'''
'''
for x in range(row_two):
    cell = df_final_two.iloc[x, 0]
    value = 0
    for y in range(row):
        cell_two = df_final.iloc[y, 0]
        if cell == cell_two:
            value +=1
    if value == 0:
        df_final_two = df_final_two.drop(df.index[x])
'''

#print(df_final["Data"].shape[0])
#print(df_final_two["Data.3"])
#print(df_final)
