from estd_connection import estd_connection
from read_csv import read_csv

data = read_csv()
cursor = estd_connection()

for each in data[:5]:
    first_data = each
    date = first_data["date"]
    symbol = first_data["symbol"]
    name = first_data["name"]
    high = first_data["high"]
    low = first_data["low"]


print(first_data)
sql = f"""
INSERT INTO MYSHARE(DATE, SYMBOL, NAME, HIGH, LOW)
VALUES('{date}', '{symbol}', '{name}', '{high}', '{low}')
"""

cursor.execute(sql)
print("Data inserted successfully!!")