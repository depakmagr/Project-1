from estd_connection import estd_connection

cursor = estd_connection()
sql = """SELECT * FROM MYSHARE"""

cursor.execute(sql)
result = cursor.fetchall()
print(result)