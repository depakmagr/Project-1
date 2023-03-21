from estd_connection import estd_connection
cursor = estd_connection()

sql = """
DELETE FROM MYSHARE 
WHERE SYMBOL = 'HIDCL'
"""
cursor.execute(sql)
print("Deleted Successfully!!!")
