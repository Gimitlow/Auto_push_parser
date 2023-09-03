from telebot import TeleBot, types
import requests
import text_collection

bot = TeleBot('')
admin_key = ''
channel = ''

class BotCollection:

	def new_post(self, image, name, new_price, old_price, url):
		name_p = name.replace('*', '')
		text = text_collection.get_text(name_p, new_price, old_price, url)
		try_image = image.replace('wc350/','')
		try:
			print(text)
			bot.send_photo(channel, try_image, text, parse_mode="Markdown")
		except Exception as e:
			bot.send_photo(channel, image, text, parse_mode="Markdown")

	def set_position(self, count):
		file = open("bot_memory.conf", "w")
		file.write(str(count))
		file.close()

	def get_position(self):
		file = open("bot_memory.conf")
		x = file.readline()
		file.close()
		return x

	def check_all(self):
		file = open("bot_memory.conf")
		x = file.readline()
		file.close()
		return x
		