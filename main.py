import parser_ozon
import crud
import time
import bot

ozon_obj = parser_ozon.OParser()
telegram_bot = bot.BotCollection()
database = crud
delay = 10
count_on_current_page = 0

class OzonEngine:
	def push_to_databse(url):
		products = ozon_obj.get_products(url)
		count = len(products)
		count_on_current_page = count
		print("Будет добавлено "+str(count)+" товаров.")
		for i in range(count):
			if database.CRUD().find(products[i]['Name']) == 'no':
				database.CRUD(products[i]['Name'], products[i]['URL'], products[i]['Img'], products[i]['New_price'], products[i]['Old_price']).create()
		return "ok"

	def memory_position_set(count):
		file = open("init.conf", "w")
		file.write(str(count))
		file.close()

	def memory_position_get():
		file = open("init.conf")
		x = file.readline()
		file.close()
		return x

	def bot_engine(count):
		for i in range(count):
			position = telegram_bot.get_position()
			data = database.CRUD().read(position)
			new_name = data[0][1].replace('уцененный товар', '').replace('УЦЕНЕННЫЙ ТОВАР', '').replace('Товар уцененный', '').replace('ТОВАР УЦЕНЕННЫЙ', '').replace('Уцененный товар', '')
			
			telegram_bot.new_post(data[0][3], new_name, data[0][4], data[0][5], data[0][2])
			telegram_bot.set_position(int(position)+1)
			
			time.sleep(10)
			

	def main_engine_func():
		print("Инициация работы модуля парсера Озон...")
		#Получение позиции страницы каталога
		count = OzonEngine.memory_position_get()
		print("Позиция страницы - "+ str(count) +"\nСтарт цикла, задержка "+ str(delay))
		#Проверка прошлой сессии, доброска недоброшенных значений
		
		last_posting_count = telegram_bot.check_all()
		db_count = database.CRUD().return_all()

		to_old_post = int(db_count[0][0]) - int(last_posting_count)

		if to_old_post > 0:
			print("Будет запощено " +str(to_old_post)+ " постов прошлой сессии, прежде чем начнется новая.")
			OzonEngine.bot_engine(to_old_post)
		else:
			print("Проверка успешна, восстановление сессии.")

		var = 1 #технический параметр для бесконечного цикла

		while var == 1:  #бесконечный цикл
			control_result = OzonEngine.push_to_databse(f"https://www.ozon.ru/category/utsenennyy-tovar/?page={ str(count) }")
			if control_result == "ok":
				count = int(count) + 1

				last_posting_count = telegram_bot.check_all()
				db_count = database.CRUD().return_all()
				to_old_post = int(db_count[0][0]) - int(last_posting_count)
				
				OzonEngine.memory_position_set(str(count))
				OzonEngine.bot_engine(to_old_post)
				time.sleep(delay)
			else:
				print("Ошибка выполнения в цикле. Завершение работы")
				break 

if __name__ == "__main__":
	OzonEngine.main_engine_func()