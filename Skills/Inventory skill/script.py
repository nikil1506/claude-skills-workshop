import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS cricket_equipments")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cricket_equipments (
        equipment_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        total_number INTEGER
    )
""")

cursor.execute("""
    SELECT name FROM sqlite_master
    WHERE type = 'table' AND name = 'cricket_equipments'
""")
print("Table exists:", cursor.fetchone() is not None)
cursor.execute(
    "INSERT INTO cricket_equipments (equipment_id, name, total_number) VALUES (?, ?, ?)",
    ("289B", "Bat", 60)
)
more_cricket_equipments = [
    ("112A", "Ball", 150),
    ("340C", "Helmet", 25),
]
cursor.executemany(
    "INSERT INTO cricket_equipments (equipment_id, name, total_number) VALUES (?, ?, ?)",
    more_cricket_equipments
)

connection.commit()

cursor.execute("SELECT * FROM cricket_equipments")
for row in cursor.fetchall():
    print(row)

connection.close()