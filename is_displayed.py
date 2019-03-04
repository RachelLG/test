from selenium import webdriver
from time import sleep, ctime

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

print(ctime())
for i in range(10):
	try:
		el = driver.find_element_by_id("kw2222222222")
		if el.is_displayed():
			break
	except:
		sleep(1)
if(i == 9):
	print("time out")
print(ctime())