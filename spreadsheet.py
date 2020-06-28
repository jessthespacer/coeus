#you need to pip install gspread oauth2client
#in order to use this script

import gspread
from oauth2client.service_acount import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('UserSearch-d26bd5aa4998.json', scope)
client = gspread.authorize(creds)

sheet = client.open('User_Search').sheet1

pp = pprint.PrettyPrinter()
all_data = get_all_records()

#finds the total number of rows (entries) entered in the first column
num = len(sheet.col_values(1))

#finds the results from the latest row entry
result = sheet.row_values(num)

return result