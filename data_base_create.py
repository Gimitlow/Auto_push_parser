import sqlite3

db = sqlite3.connect('products_base.db')
c = db.cursor()

c.execute("""CREATE TABLE products (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			name text,
			url text,
			image text,
			new_price text,
			old_price text,
			posting text
			)""")