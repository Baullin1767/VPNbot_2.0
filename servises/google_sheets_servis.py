import httplib2
import asyncio
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from data_base import db

CREDENTIALS_FILE = 'vpn-bot-users-fc6663caf92b.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets',
                                                                                  'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())
service = discovery.build('sheets', 'v4', http = httpAuth)

spreadsheetId = '1C7aQ8f78wnF8OFuiERt-qHx9zf9qz5rMO-Sls6x9Jj0'



results = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheetId, body = {
  "requests": [

    # Задать ширину столбца A: 317 пикселей
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": 0,
          "dimension": "COLUMNS",  # COLUMNS - потому что столбец
          "startIndex": 0,         # Столбцы нумеруются с нуля
          "endIndex": 1            # startIndex берётся включительно, endIndex - НЕ включительно,
                                   # т.е. размер будет применён к столбцам в диапазоне [0,1), т.е. только к столбцу A
        },
        "properties": {
          "pixelSize": 150     # размер в пикселях
        },
        "fields": "pixelSize"  # нужно задать только pixelSize и не трогать другие параметры столбца
      }
    }
  ]
}).execute()

async def update_table():
    values = [['Дата окончания пробного периода','Дата оплаты','Имя','ID', 'Сервер']]
    users=db.get_users()
    for u in users:
        date_of_arrival = u[2]
        date_sub = u[4]
        user_id = u[0]
        full_name = u[1]
        server = u[-1]
        values.append([date_of_arrival, date_sub, full_name, f'#ID{user_id}', server])
    results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheetId, body = {
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "Лист1",
             "majorDimension": "ROWS",     # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
             "values": values}
        ]
    }).execute()