import MySQLdb
connection = MySQLdb.connect(host='localhost',db='myapp',user='root',passwd='root', port=33061,unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock")
cursor = connection.cursor()
# SQL
cursor.execute("select * from tweets")
result = cursor.fetchall()
print result
# for row in result:
#     p row[0]

cursor.close()
connection.close()
