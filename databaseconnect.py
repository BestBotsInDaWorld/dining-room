from mysql.connector import connect

mydb = connect(host='localhost',
               port='3306',
               user='root',
               database='dining-room')

print(mydb)