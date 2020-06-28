import gspread
from oauth2client.service_acount import ServiceAccountCredentials
import pprint
import spreadsheets
import sqlite3

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

#espablishing connection to database
connection = sqlite3.connect("people.db")

#creatinc cursor
crsr = connection.cursor()


import unichoice as u_lan
import subjectandlang_chosen as s_lan
import countryandlang_chosen as c_lan
import languagechosenonly as o_lan

if (result[3] != "na"):
	if (result[2] != "na"):
		crsr.execute(c_lan)
	elif(result[1] != "NONE"):
		crsr.execute(s_lan)
	elif(result[0] != "NONE"):
		crsr.execute(u_lan)
	else:
		crsr.execute(o_lan)

connection.commit()
connection.close()

