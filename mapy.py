import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_security.json',scope)
client = gspread.authorize(creds)

sheet = client.open('SOUPIS OBJEKTY').sheet1

tabulka = sheet.get_all_records()

jmeno = "a"
i=2

with open('data.json', mode = 'w',encoding='UTF-8') as f:
    f.write("{\n")
    while jmeno !="":
    # for i in range(3,6):
        i += 1
        jmeno = sheet.cell(i, 2).value
        poloha = sheet.cell(i, 23).value
        obec = sheet.cell(i, 3).value
        kapacita = sheet.cell(i, 5).value
        vytopitelnost1 = sheet.cell(i, 6).value
        vytopitelnost2 = sheet.cell(i, 7).value
        cas = sheet.cell(i, 9).value
        km = sheet.cell(i, 11).value
        cena = sheet.cell(i, 13).value
        odkaz = sheet.cell(i, 16).value
        poznamka = sheet.cell(i, 24).value
        misto = sheet.cell(i, 1).value

        print(jmeno)

        vystup = '"{}":{{"poloha":"{}","obec":"{}","kapacita":"{}","vytopitelnost1":"{}","vytopitelnost2":"{}","cas":"{}","km":"{}","cena":"{}","odkaz":"{}","poznamka":"{}","misto":"{}"}},\n' \
                 ''.format(jmeno,poloha,obec,kapacita,vytopitelnost1,vytopitelnost2,cas,km,cena,odkaz,poznamka, misto)

        f.write(vystup)
    f.write('"konec":{"poloha":""}\n}')
