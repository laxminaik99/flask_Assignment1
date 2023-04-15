import sqlite3

connection=sqlite3.connect("./instance/companytable.db")
cursor=connection.cursor()

with open('combined_csv2.csv','r') as file:
 records=0
 for row in file:
    #  cursor.execute("INSERT INTO Price_History({cols}) VALUES({vals});".format(cols = str(data.keys()).strip('[]'), 
    #                 vals=str([data[i] for i in data]).strip('[]')
    #                 ))
    cursor.execute("INSERT INTO CompanyModel(`Date`,`Open`,`High`,`Low`,`Close`,`Adj_Close`,`Volume`,`filename`) VALUES (?,?,?,?,?,?,?,?)", row.split(","))
    connection.commit()
    records+=1
connection.close()
print('{} Records transfer completed'.format(records))
