import sqlite3
conn = sqlite3.connect('Containers.db')
c = conn.cursor()
anne = c.execute("SELECT cdocs FROM containers")
row = [item[0] for item in anne]
print(sum(row))