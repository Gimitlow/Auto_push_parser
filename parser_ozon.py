from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

o = Options()
#o.add_argument('--headless=new')
#o.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=o)

#Интерфейс парсера
class IOzonParser():

	def get_name(self, id):
		name = driver.find_element("xpath", '//*[@id="paginatorContent"]/div/div/div['+ str(id) +']/div[2]/div/a/div/span').text
		return name

	def get_url(self, id):
		find_url = driver.find_element("xpath", '//*[@id="paginatorContent"]/div/div/div['+ str(id) +']/div[2]/div/a')
		url = find_url.get_attribute('href')
		return url

	def get_image(self, id):
		image = driver.find_element("xpath", '//*[@id="paginatorContent"]/div/div/div['+ str(id) +']/div[1]/a/div/div[1]/img')
		src_image = image.get_attribute('src')
		return src_image

	def get_new_price(self, id):
		new_price = driver.find_element("xpath", '//*[@id="paginatorContent"]/div/div/div['+  str(id) +']/div[3]/div[1]/div/span[1]').text
		return new_price

	def get_old_price(self, id):
		try:
			old_price = driver.find_element("xpath", '//*[@id="paginatorContent"]/div/div/div['+ str(id) +']/div[3]/div[1]/div/span[2]').text
			return old_price
		except Exception as e:
			return ""
			
	def go_to(self, url):
		driver.get(url)
		return 'ok'

	def restart(self):
		driver.close()
		capabilities = o.to_capabilities()
		driver.start_session(capabilities)
		return 'ok'

#Движок парсера
class OParser(IOzonParser):
	#Возвращает 36 позиций товара со страницы
	def get_products(self, url):
		self.restart()
		self.go_to(url)
		time.sleep(10)

		product_array = []	
		
		for i in range(35):
			product = {
				'Name': self.get_name(i+1),
				'URL': self.get_url(i+1),
				'Img': self.get_image(i+1),
				'New_price': self.get_new_price(i+1),
				'Old_price': self.get_old_price(i+1)
			}
			product_array.append(product)

		print(product_array)
		return product_array