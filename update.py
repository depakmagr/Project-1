from estd_connection import estd_connection
cursor = estd_connection()


sql = """
UPDATE MYSHARE SET 
NAME = 'Arun Valley Hydropower Development Co. Ltd.'                                                        
WHERE SYMBOL = 'HIDCL'
"""


cursor.execute(sql)

print("Update Successfully!!")