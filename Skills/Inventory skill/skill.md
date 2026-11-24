name: Iventory-Handler
description: Maintain the cricket equipment inventory in inventory.db: add, remove, update quantities, list or search items when the user asks.
The data lives in the SQLite file `inventory.db`, in the table `cricket_equipments`:

| column | type | notes |
|---|---|---|
| equipment_id | TEXT PRIMARY KEY | unique code, e.g. "289B" |
| name | TEXT NOT NULL | e.g. "Bat", "Ball", "Helmet" |
| total_number | INTEGER | quantity in stock |
## Rules (always follow)

1. Never run `DROP TABLE`, and never run `DELETE` without a WHERE clause. This is the user's real inventory, and recreating the table would erase it.
2. Create the table only with `CREATE TABLE IF NOT EXISTS` (same schema as above), so it is safe to run every time.
3. Use parameterized queries (`?` placeholders). Never paste user text directly into an SQL string.
4. Call `connection.commit()` after every change, and always close the connection.
5. Before removing an item, show the user the matching row and ask for confirmation.
6. After any change, SELECT the affected row(s) and tell the user the result.

## Operations

- **Add**: `INSERT INTO cricket_equipments (equipment_id, name, total_number) VALUES (?, ?, ?)`. If the equipment_id already exists (IntegrityError), tell the user and ask whether to update the quantity instead.
- **Remove**: `DELETE FROM cricket_equipments WHERE equipment_id = ?`, only after confirmation. If `cursor.rowcount == 0`, say the item was not found.
- **Update quantity**: `UPDATE cricket_equipments SET total_number = ? WHERE equipment_id = ?` for an exact number. For "add 10 balls" or "used 2 helmets", use `SET total_number = total_number + ?` (a negative number for removals). Refuse any change that would make the quantity negative.
- **List**: `SELECT * FROM cricket_equipments ORDER BY name`. Show the result as a small table.
- **Search**: `SELECT * FROM cricket_equipments WHERE name LIKE ?` with `'%' + term + '%'`, or search by equipment_id.

## Finding the right item

Users will usually say a name ("bat"), not an ID. Search by name first. If more than one row matches, list them and ask which one. If none match, say so instead of guessing.

## Reply style

Keep replies short. Say what changed (quantity before and after) and show the current row. Don't print the whole table unless the user asks for a list.