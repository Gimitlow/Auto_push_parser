import sqlite3

db = sqlite3.connect('products_base.db')
c = db.cursor()

class CRUD:
	#конструктор класса, определяет параметры записи
	def __init__(self, name=None, url=None, image=None, new_price=None, old_price=None, posting="no"):
		self.name_db = name
		self.url_db = url
		self.image_db = image
		self.new_price_db = new_price
		self.old_price_db = old_price
		self.posting_db = posting

	#создание записи
	def create(self):
		product_name = self.name_db
		name = product_name.replace('\'','')

		c.execute(f"INSERT INTO products (name, url, image, new_price, old_price, posting) VALUES ('{name}', '{self.url_db}' , '{self.image_db}', '{self.new_price_db}', '{self.old_price_db}', '{self.posting_db}')")
		db.commit()
		return(f"Запись {self.name_db} была добавлена в базу.")

	#Поиск повторений
	def find(self, product_name):
		name = product_name.replace('\'','')

		c.execute(f"SELECT * FROM products WHERE name = '{name}'")
		data = c.fetchall()
		if bool(data) == False:
			return 'no'
		else:
			return 'yes'

	#Возвращает массив данных для бота
	def read(self, id):
		c.execute(f"SELECT * FROM products WHERE rowid = '{id}'")
		data = c.fetchall()
		return data

	def return_all(self):
		c.execute(f"SELECT COUNT(*) FROM products")
		data = c.fetchall()
		return data

	#удаление записи
	def delete(self, id):
		c.execute(f"DELETE FROM products WHERE rowid = {id}")
		db.commit()
		return(f"Запись {id} была удалена")

#Структура базы
#c.execute("""CREATE TABLE products (
#			id INTEGER PRIMARY KEY AUTOINCREMENT,
#			name text,
#			image text,
#			new_price text,
#			old_price text,
#			posting text
#			)""")

#Добавление записи
#c.execute("INSERT INTO products (name, image, new_price, old_price) VALUES ('test', 'test', '1', '2')")

#Найти поле
#c.execute("SELECT id, name FROM products")
#print(c.fetchall()) - взять все из столбца
#print(c.fetchmany(1)) - взять определеное

#Удаление
#c.execute("DELETE FROM products WHERE id = 1")

#Обновление данных 
#c.execute("UPDATE products SET name = 'okey_now' WHERE id = 5")

#Запушить данные
#db.commit()
#Закрыть соединение
#db.close()