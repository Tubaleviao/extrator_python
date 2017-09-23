import pyodbc
import csv
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.1.33;DATABASE=BASE_DE_DADOS;UID=USUARIO;PWD=SENHA')
cursor = cnxn.cursor()
cursor.execute("select * from TABLE")
rows = cursor.fetchall()
data = []
for row in rows:
    	data.append([row.COLUMN1.strip(), row.COLUMN2.strip()])
with open('saida.csv', 'wb') as fp:
    a = csv.writer(fp, delimiter=';')
    a.writerows(data)